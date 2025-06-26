# src/ai_engine.py

import os

# Use a flag to check if imports were successful
try:
    import torch
    from transformers import GPT2LMHeadModel, GPT2Tokenizer
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False

class AIEngine:
    """Handles offline text generation using a local GPT-2 model."""
    def __init__(self, model_path="./models/gpt2"):
        self.model = None
        self.tokenizer = None
        self.device = None

        if not TRANSFORMERS_AVAILABLE:
            print("AI Engine Warning: 'transformers' or 'torch' not found. AI features will be disabled.")
            return

        if not os.path.exists(model_path):
            print(f"AI Engine Warning: Model not found at '{model_path}'.")
            print("Run 'python download_model.py' first. AI features will be disabled.")
            return

        print("AI Engine: Initializing...")
        try:
            # Check for CUDA GPU and set device
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            print(f"AI Engine: Using device: {self.device}")

            self.tokenizer = GPT2Tokenizer.from_pretrained(model_path)
            self.model = GPT2LMHeadModel.from_pretrained(model_path)
            self.model.to(self.device) # Move model to GPU if available
            print("AI Engine: Model loaded successfully.")
        except Exception as e:
            print(f"AI Engine Error: Failed to load model. {e}")
            self.model = None # Ensure model is None on failure

    def generate_text(self, prompt, max_length=100):
        """Generates text based on a prompt."""
        if self.model is None or self.tokenizer is None:
            return "AI model is not available. Using fallback description."

        try:
            inputs = self.tokenizer.encode(prompt, return_tensors='pt').to(self.device)
            outputs = self.model.generate(
                inputs,
                max_length=max_length,
                num_return_sequences=1,
                no_repeat_ngram_size=2, # Prevents repetitive phrases
                top_k=50, # Limits selection to top 50 words
                top_p=0.95, # Nucleus sampling
                temperature=0.8 # Controls randomness
            )
            generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return generated_text
        except Exception as e:
            print(f"AI Engine Error: Could not generate text. {e}")
            return "An error occurred during AI text generation."