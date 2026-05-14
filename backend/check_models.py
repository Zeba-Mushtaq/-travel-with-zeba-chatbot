import google.generativeai as genai
import os

# Your API key
os.environ["GEMINI_API_KEY"] = "AIzaSyA_M_S8-vR39N6sBw6ULrx5IYjtMvCXKEw"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# List all available models
print("Available models for your API key:\n")
for model in genai.list_models():
    print(f"Model: {model.name}")
    print(f"Display Name: {model.display_name}")
    print(f"Description: {model.description}")
    print("-" * 50)
