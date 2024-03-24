import argparse
from model import ModelHandler
from utilities import clean_response, ensure_coherent_ending, speak, print_response, start_typing_animation, stop_typing_animation
from config import default_model

def main():
    parser = argparse.ArgumentParser(description="Chat with Tim, an AI assistant.")
    parser.add_argument("--model", type=str, default=default_model, help="Model type to use.")
    parser.add_argument("--speak", action="store_true", help="Enable speech output.")
    parser.add_argument("--temp", type=float, default=0.7, help="Temperature for response generation.")
    parser.add_argument("--top_k", type=int, default=50, help="Top-K filtering for response generation.")
    parser.add_argument("--tokens", type=int, default=300, help="Maximum new tokens to generate.")
    parser.add_argument("--top_p", type=float, default=0.9, help="Top-P filtering for response generation.")
    parser.add_argument("--max_length", type=int, default=100, help="Maximum length of the generated response.")
    args = parser.parse_args()

    model_handler = ModelHandler(args.model, args)

    print("Tim: Hi, I'm Tim. What is on your mind?")
    prompt_type = "> "
    while True:
        print()
        user_input = input(prompt_type)
        if user_input.lower() == 'exit':
            break

        animation_thread = start_typing_animation()  # Start the animation immediately

        generated_text = model_handler.generate_text(user_input)  # Pass the prompt to the model
        cleaned_text = clean_response(generated_text)
        final_text = ensure_coherent_ending(cleaned_text)

        stop_typing_animation(animation_thread)  # Stop the animation

        if args.speak:
            speak(final_text)
        print_response(final_text)  # Print Tim's response
        prompt_type = ">> " if final_text.endswith('?') else "> "

if __name__ == "__main__":
    main()