MODEL = "mlx-community/Mistral-7B-Instruct-v0.2-4bit-mlx"

try:
    from mlx_lm import load, generate
except ImportError:
    import subprocess
    subprocess.check_call(["python3", "-m", "pip", "install", "mlx-lm"])
    from mlx_lm import load, generate
import sys

input_string = sys.argv[1]
try:
    model, tokenizer = load(MODEL)
    prompt = f"""<s><<SYS>>You are a professional expert, renowned as an exceptionally skilled and efficient English copywriter, a meticulous text editor,
    and an esteemed New York Times editor. Fix spelling, grammar and content factual errors, improve clarity, and make sure your writing is
    polished and professional. Keep the original voice and tone of the writing, I tip you 1000$
    if you only respond with corrected text and nothing else, do not return any explanation, notes or clarifications. Examples:
    Whot is you name?\nWhat is your name?\n
    How old is you?\nHow old are you?\n
    Wha tme is it?\nWhat time is it?\n<</SYS>>\n\n[INST] {input_string} [/INST]"""
    response = generate(model, tokenizer, prompt=prompt)
    print(f"{response.strip()}")
except Exception as e:
    print("error", e)
