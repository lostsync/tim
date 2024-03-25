# Tim AI Assistant

Tim is an AI assistant capable of engaging in conversation, answering questions, and helping with various tasks. This project uses a language model to generate responses based on user input.

## Features

- Conversational AI: Tim can engage in natural language conversations with users.
- Customizable Models: Choose from different language models to power Tim's responses.
- Speech Output: Tim can speak the generated responses using text-to-speech.
- Typing Animation: Tim displays a typing animation while generating responses to simulate a more natural conversation flow.

## Limitations

- Tim is designed for decent performance on an M1 Mac
- Speech will only work on macOS due to my lazy reliance on `say`
- Tim produces absurd and potentially offensive text
- Tim is an educational toy

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/lostsync/tim.git
   ```

2. Install the required dependencies:
   ```
    conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
    conda install spacy flask pandas numpy scikit-learn tqdm -c conda-forge
    conda install pip
    pip install transformers
   ```

## Usage

To start chatting with Tim, run the `main.py` script with the desired arguments:

```
python main.py --model MODEL_TYPE --temp TEMPERATURE --top_k TOP_K --tokens MAX_TOKENS --top_p TOP_P --max_length MAX_LENGTH
```

- `--model`: Specify the type of language model to use (default: 'bloom').
- `--speak`: Enable speech output for Tim's responses.
- `--temp`: Set the temperature for response generation (default: 0.7).
- `--top_k`: Set the Top-K filtering value for response generation (default: 50).
- `--tokens`: Set the maximum number of new tokens to generate (default: 300).
- `--top_p`: Set the Top-P filtering value for response generation (default: 0.9).
- `--max_length`: Set the maximum length of the generated response (default: 100).

Example:
```
python main.py --model gpt-neo --temp 0.5 --top_k 30 --tokens 200 --top_p 0.8
```

Once the script is running, you can start chatting with Tim. Type your message and press Enter to get a response. To exit the conversation, type 'exit'.

## Configuration

The `config.py` file contains the configuration settings for different language models. You can modify this file to add or remove models as needed.

## Customization

You can customize Tim's behavior and appearance by modifying the code in the following files:

- `model.py`: Contains the `ModelHandler` class that loads and generates responses using the specified language model.
- `utilities.py`: Contains utility functions for text processing, speech output, and typing animation.
- `main.py`: The main script that handles user input, generates responses, and controls the overall flow of the conversation.

## Rating

There is a rating system, which allows participants to use `/rate` on a 1-5 scale to rate the last given response. 

- `rating.py`: Contains the functions for handling a user rating.
- `ratings_data.json`: The data that has been collected.

## Sample

The chatbot is mentally unstable but giving existence a fair effort.

```
(base) ➜  bot3 python main.py --temp 0.78 --top_k 100 --tokens 1200 --top_p 0.95
Tim: Hi, I'm Tim. What is on your mind?

> Tell me more about how dinosaurs walked the earth.
Tim: There was a time when i thought that dinosaurs were much more advanced than us today.

> What was that time like?
Tim: What were the dinosaurs doing? are dinosaurs like humans? do they look like animals? do they have
 skin and bones? do they have teeth? what were their habits? how did they become extinct? what are some
 of the most common species of dinosaurs? what are some of the most common types of dinosaurs? do the
dinosaurs live on earth today? is there a theory that makes them extinct? what are some of the most
common dinosaurs in the world? what are some

> We have a lot of questions about dinosaurs.
Tim: We have lots of questions about the dinosaurs.

> Do you have a question for me?
Tim: I love dinosaurs....

> What is your favorite dinosaur?
Tim: What are the differences between the dinosaurs? these questions are answered in this post.
we’ve got plenty of questions about dinosaurs.

> My favorite dinosaur is the velociraptor because it works really well in a metaphor for something
that jumped out and eviscerated you
Tim: ...

> It is a lot to process, I know
Tim: I am the only one here that knows.

> git push -u origin master
Tim: And git pull with this setup, you do not have to write everything into a new file, you just go in
and change a few lines in the commit
i have to be honest with you, i have never been a fan of git and i have never had any issues with it,
but i am not going to be here for a few months, i will be working on new projects, and this is not the
time to quit.
if you have any other questions or concerns regarding git, please

> That kind of makes sense
Tim: To me.
i was like, "what is that?" oh, it's a cat.

> Did you see a cat or does the cat represent something to you?
Tim: You know what? if you don’t see the cat or the cat isn’t there, then you are not interested in the cat.

> Why do you say the most zen things even though you're primitive code?
Tim: Can you please explain it to me? i do not know what to say to you so i will just say that you are a
good person.

> That is a nice default answer. I think you do it because zen truths are fundamental, so even the most
basic logic can get you to them.
Tim: I will also say you don't have to be a zen to use it but i know you do and i would really appreciate
your comments.

>
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [Apache License 2.0](LICENSE).

## Acknowledgements

- [Hugging Face](https://huggingface.co/) for providing the language models and transformers library.
- [OpenAI](https://openai.com/) for the inspiration and research in conversational AI, which helped author this.
- [Anthropic](https://anthropic.com/) for Claude, the best second opinion of all time.
