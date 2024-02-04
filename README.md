# Autogram

## Ollama Backend

### Installation

Install [ollama](https://ollama.ai/)

Run in the background:

```bash
ollama run mistral-grammar-checker
```
Install the workflow. This essentially copies the workflow to `~/Library/Services/autogram-ollama.workflow`.

<img src="assets/step1.jpg" style="max-width: 500px;" />

<img src="assets/step2.jpg" style="max-width: 300px;" />

Go to System Preferences -> Keyboard -> Shortcuts -> Services -> General -> autogram, and set the shortcut, in my case I set it to `⌃⌥⌘G`.

<img src="assets/step3.jpg" style="max-width: 300px;" />

<img src="assets/step4.jpg" style="max-width: 500px;" />

### Usage

In any OSX application, select some text, and press the shortcut you set. The selected text will be replaced with the generated text from the model.

## Apple MLX Backend

Install `autogram-mlx.workflow` the same way as above, no need to edit and add token, however you may edit `MODEL="mistral"`, in case you want to use a different model

<img src="assets/stepmlx.jpg" width="500"/>