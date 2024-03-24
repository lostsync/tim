# Tim AI Assistant

Tim is an AI assistant capable of engaging in conversation, answering questions, and helping with various tasks. This project uses a language model to generate responses based on user input.

## Features

- Conversational AI: Tim can engage in natural language conversations with users.
- Customizable Models: Choose from different language models to power Tim's responses.
- Speech Output: Tim can speak the generated responses using text-to-speech.
- Typing Animation: Tim displays a typing animation while generating responses to simulate a more natural conversation flow.

## Limitations

- Tim is designed for decent performance on an M1 Mac
- Tim produces absurd and potentially offensive text
- Tim is an educational toy

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/lostsync/tim.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
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

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [Apache License 2.0](LICENSE).

## Acknowledgements

- [Hugging Face](https://huggingface.co/) for providing the language models and transformers library.
- [OpenAI](https://openai.com/) for the inspiration and research in conversational AI.
