models = {
    'gpt2': {
        'model_name': 'gpt2-medium',
        'model_class': 'GPT2LMHeadModel',
        'tokenizer_class': 'GPT2Tokenizer'
    },
    'gpt-neo': {
        'model_name': 'EleutherAI/gpt-neo-1.3B',
        'model_class': 'GPTNeoForCausalLM',
        'tokenizer_class': 'GPT2Tokenizer'
    },
    'bloom': {
        'model_name': 'bigscience/bloom-560m',
        'model_class': 'BloomForCausalLM',
        'tokenizer_class': 'BloomTokenizerFast'
    },
    'flan-t5': {
        'model_name': 'google/flan-t5-base',
        'model_class': 'T5ForConditionalGeneration',
        'tokenizer_class': 'T5Tokenizer'
    },
    'distilbert': {
        'model_name': 'distilbert-base-uncased',
        'model_class': 'DistilBertForQuestionAnswering',
        'tokenizer_class': 'DistilBertTokenizer'
    }
}

default_model = 'bloom'