# download_model.py

import os
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def download_and_save_model():
    """
    Downloads the GPT-2 model and tokenizer from Hugging Face
    and saves them to a local directory for offline use.
    """
    model_name = "gpt2"
    local_model_path = "./models/gpt2"

    print(f"Attempting to download model: {model_name}")
    print(f"This will be saved to: {local_model_path}")
    print("This may take a few minutes and requires an internet connection...")

    try:
        # Create directory if it doesn't exist
        if not os.path.exists(local_model_path):
            os.makedirs(local_model_path)

        # Download and save the model and tokenizer
        model = GPT2LMHeadModel.from_pretrained(model_name)
        tokenizer = GPT2Tokenizer.from_pretrained(model_name)

        model.save_pretrained(local_model_path)
        tokenizer.save_pretrained(local_model_path)

        print("\nModel and tokenizer downloaded successfully!")
        print(f"They are saved in the '{local_model_path}' directory.")
        print("You can now run the main game application offline.")

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please check your internet connection and try again.")
        print("The 'transformers' library must be installed first (pip install transformers).")

if __name__ == "__main__":
    download_and_save_model()