MODEL = "mistral-grammar-checker:latest"

try:
    import ollama
except ImportError:
    import subprocess
    subprocess.check_call(["python3", "-m", "pip", "install", "ollama"])
    import ollama
import sys

input_string = sys.argv[1]
try:
    response = ollama.generate(model= MODEL, prompt=input_string)
    response = response['response']
    print(f"{response.strip()}")
except Exception as e:
    print("error", e)