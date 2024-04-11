import os
import time
import psutil
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


def load_model_and_tokenizer(model_name, cache_directory):
    print("Loading model...")
    llm_model = AutoModelForCausalLM.from_pretrained(
        model_name, cache_dir=cache_directory
    )
    print("Model loaded. Loading tokenizer...")
    llm_tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_directory)
    print("Tokenizer loaded.")
    return llm_model, llm_tokenizer


def generate_text(llm_pipeline, prompt, max_response_length):
    print("Generating text...")
    start_time = time.time()
    start_memory = psutil.virtual_memory().used
    start_cpu = psutil.cpu_percent()

    generated_text = llm_pipeline(prompt)[0]["generated_text"]

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
    # Specify your cache and model directories
    cache_directory = "./models/"

    model_name = "microsoft/phi-2"
    max_response_length = 20

    # Load the original model and tokenizer
    llm_model, llm_tokenizer = load_model_and_tokenizer(model_name, cache_directory)

    # Create the pipeline
    llm_pipeline = pipeline(
        "text-generation",
        model=llm_model,
        tokenizer=llm_tokenizer,
        max_length=max_response_length,
    )

    prompt = input("Prompt: ")

    # Generate text using the original model
    generated_text, time_taken, memory_used, cpu_used = generate_text(
        llm_pipeline, prompt, max_response_length
    )

    # Print the generated text
    print("Generated text:")
    print(generated_text)

    # Print the resources used and time taken
    print(f"Time taken: {time_taken} seconds")
    print(f"Memory used: {memory_used} bytes")
    print(f"CPU used: {cpu_used} percent")


if __name__ == "__main__":
    main()
