import os
import time
import psutil
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Specify your cache and model directories
cache_directory = "./models/"
model_name = "mistralai/Mistral-7B-v0.1"
max_response_length = 20
use_fast_tokenizer = True  # Variable to control the use of the fast tokenizer

# Load the original model and tokenizer
print("Loading model...")
llm_model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=cache_directory)
print("Model loaded. Loading tokenizer...")
llm_tokenizer = AutoTokenizer.from_pretrained(
    model_name, cache_dir=cache_directory, use_fast=use_fast_tokenizer
)
print("Tokenizer loaded.")


def generate_text(llm_model, llm_tokenizer, prompt, max_response_length):
    print("Generating text...")
    start_time = time.time()
    start_memory = psutil.virtual_memory().used
    start_cpu = psutil.cpu_percent()

    # Tokenize the prompt
    inputs = llm_tokenizer.encode(prompt, return_tensors="pt")

    # Generate text using the model
    with torch.no_grad():
        outputs = llm_model.generate(inputs, max_length=max_response_length)

    # Decode the output
    generated_text = llm_tokenizer.decode(outputs[0])

    end_time = time.time()
    end_memory = psutil.virtual_memory().used
    end_cpu = psutil.cpu_percent()

    return (
        generated_text,
        end_time - start_time,
        end_memory - start_memory,
        end_cpu - start_cpu,
    )


def main():
    prompt = input("Prompt: ")

    total_memory = psutil.virtual_memory().total
    # Generate text using the original model
    generated_text, time_taken, memory_used, cpu_used = generate_text(
        llm_model, llm_tokenizer, prompt, max_response_length
    )

    # Print the generated text
    print("Generated text:")
    print(generated_text)

    # Print the resources used and time taken
    print(f"Time taken: {time_taken} seconds")
    print(
        f"Memory used: {memory_used} bytes out of {total_memory} bytes ({memory_used/total_memory*100:.2f}%)"
    )
    print(f"CPU used: {cpu_used} percent")


if __name__ == "__main__":
    main()
