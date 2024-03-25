from transformers import (
    AutoTokenizer, 
    AutoModelForSeq2SeqLM, 
    AutoModelForCausalLM, 
    AutoModelForQuestionAnswering, 
    DistilBertForQuestionAnswering,
    T5ForConditionalGeneration
)
import torch
from config import models, default_model
import os

class ModelHandler:
    def __init__(self, model_type, args):
        os.environ["TOKENIZERS_PARALLELISM"] = "false"
        
        model_config = models.get(model_type, models[default_model])
        model_name = model_config['model_name']
        model_class = model_config['model_class']
        tokenizer_class = model_config['tokenizer_class']

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Adjust tokenizer settings as needed
        self.tokenizer.pad_token = self.tokenizer.eos_token or self.tokenizer.pad_token or '[PAD]'
        self.tokenizer.add_special_tokens({'pad_token': self.tokenizer.pad_token})
        self.tokenizer.model_max_length = 1000000  # Set a large value for max_length

        # Identify model type and load the appropriate model
        if 'ForQuestionAnswering' in model_name:
            self.model = AutoModelForQuestionAnswering.from_pretrained(model_name)
        elif 't5' in model_name.lower() or 'pegasus' in model_name.lower() or 'bart' in model_name.lower() or 'mT5' in model_name.lower():
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        else:
            self.tokenizer.padding_side = 'left'
            self.model = AutoModelForCausalLM.from_pretrained(model_name)



        # if model_class == 'DistilBertForQuestionAnswering':
        #     self.tokenizer.pad_token = self.tokenizer.eos_token or '[PAD]'
        #     self.tokenizer.add_special_tokens({'pad_token': '[PAD]'})
        #     self.tokenizer.model_max_length = 1000000  # Set a large value for max_length
        #     self.model = DistilBertForQuestionAnswering.from_pretrained(model_name)
        # else:
        #     self.tokenizer.pad_token = self.tokenizer.eos_token
        #     self.tokenizer.padding_side='left'
        #     self.tokenizer.model_max_length = 1000000  # Set a large value for max_length
        #     self.model = AutoModelForCausalLM.from_pretrained(model_name)
        
        self.model.to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))
        self.args = args
        self.conversation_history = []

    def generate_text(self, input_text):
        self.conversation_history.append(input_text)
        if len(self.conversation_history) > 5:
            self.conversation_history = self.conversation_history[-5:]

        prompt = " ".join(self.conversation_history)
        inputs = self.tokenizer(prompt, return_tensors='pt', padding=True, truncation=True)
        attention_mask = inputs['attention_mask'].to(self.model.device)
        input_ids = inputs['input_ids'].to(self.model.device)
        if isinstance(self.model, T5ForConditionalGeneration):
            # For T5 and similar models, you might need to adjust the prompt format
            input_ids = self.tokenizer.encode("translate English to French: "+prompt, return_tensors="pt")
            output_ids = self.model.generate(input_ids)[0]
            return self.tokenizer.decode(output_ids, skip_special_tokens=True)
        elif isinstance(self.model, DistilBertForQuestionAnswering):
            outputs = self.model(input_ids, attention_mask=attention_mask)
            start_scores = outputs.start_logits
            end_scores = outputs.end_logits
            answer_start = torch.argmax(start_scores)
            answer_end = torch.argmax(end_scores) + 1
            answer_tokens = input_ids[0, answer_start:answer_end]
            response = self.tokenizer.decode(answer_tokens)
        else:
            response = ""
            prev_sentence = ""
            for _ in range(self.args.max_length):
                outputs = self.model.generate(
                    input_ids, attention_mask=attention_mask,
                    temperature=self.args.temp, do_sample=True, top_p=self.args.top_p,
                    num_return_sequences=1, pad_token_id=self.tokenizer.eos_token_id,
                    max_new_tokens=1
                )
                new_token = self.tokenizer.decode(outputs[0][-1], skip_special_tokens=True)
                response += new_token

                # Check for repetition and incomplete sentences
                sentences = response.split('. ')
                current_sentence = sentences[-1]
                if len(sentences) > 1 and (current_sentence == prev_sentence or not current_sentence.endswith('.')):
                    response = '. '.join(sentences[:-1]) + '.'
                    break

                prev_sentence = current_sentence
                input_ids = torch.cat([input_ids, outputs[:, -1:]], dim=-1)
                attention_mask = torch.cat([attention_mask, torch.ones((1, 1), device=attention_mask.device)], dim=-1)

            response = response.replace(prompt, '').strip()

        return response