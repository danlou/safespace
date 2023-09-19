__version__ = '1.0.0+mps'  # platform specific label
import os, sys, requests, readline
from datetime import datetime as dt
os.system('cls' if os.name == 'nt' else 'clear')

from rich.progress import track
from rich.console import Console
console = Console()

default_model = "https://huggingface.co/danlou/safespace-7b-gguf/resolve/main/safespace-1.0-7b-q4_0.gguf"
ctx_size = 4096


def sys_print(text, color='bright_cyan'):
    console.print(f"[{color}][bold]>[/bold] {text}[/{color}]", highlight=False)

def user_input(max_len=2048):
    console.print('[bright_white][bold]>[/bold] ', end='')
    input_str = console.input().strip()

    if input_str in {'q', 'quit', 'exit', 'close', 'bye'}:
        sys.exit()
    elif len(input_str) == 0:
        input_str = '(no answer)'
    elif len(input_str) > max_len:  # truncate if too long
        input_str = input_str[:max_len] + '...'
    input_str = input_str.replace('ASSISTANT:', 'ASSISTANT')  # avoid injections
    
    return input_str

def download_model(url, models_dir='safespace_models/', block_sz=8192):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    model_sz = int(response.headers.get('content-length', 0))
    destination = os.path.join(models_dir, url.split('/')[-1])
    with open(destination, 'wb') as out_file:
        for chunk in track(response.iter_content(block_sz),
                           description=f"{url.split('/')[-1]} ({round(model_sz / (1024 ** 3), 2)} GB)",
                           total=model_sz//block_sz):
            out_file.write(chunk)

def get_model_path(models_dir='safespace_models/', ext='gguf'):  # models_dir in the same path as binary
    os.makedirs(models_dir, exist_ok=True)
    fns = [os.path.join(models_dir, f) for f in os.listdir(models_dir) if f.endswith(f'.{ext}')]
    if len(fns) == 0:
        sys_print("No model detected, let's download the default (only needed once).")
        download_model(default_model, models_dir)
        return os.path.join(models_dir, default_model.split('/')[-1])
    
    return max(fns, key=os.path.getmtime)  # use most recent if several found

pct_warned = {pct: False for pct in range(0, 100)}
def warn_session_length(total_tokens):
    remaining = ((ctx_size - total_tokens)/ctx_size) * 100
    if remaining <= 50 and pct_warned[50] is False:
        sys_print('[u]Note[/u]: We are half-way through our session.')
        pct_warned[50] = True
    elif remaining <= 10 and pct_warned[10] is False:
        sys_print('[u]Note[/u]: We are close to the end of our session.')
        pct_warned[10] = True
    elif remaining <= 1.0:
        sys_print('[u]Note[/u]: This session has become too large. Please start again to continue.')
        sys.exit()


if __name__ == '__main__':

    console.print(f'[bold][bright_cyan]safespace[/bright_cyan][/bold] (v{__version__}) - Private and local AI counselling.', highlight=False)
    console.print('Visit https://github.com/danlou/safespace for more details.\n')

    if '--force-download' in sys.argv[1:]:
        download_model(default_model)

    from llama_cpp import Llama
    llm = Llama(model_path=get_model_path(), n_ctx=ctx_size, verbose=False,
                use_mlock=True, use_mmap=False)  # ~5GB of RAM with default model (depends on platform)

    sys_msg = "This app is called safespace, and you are a Rogerian counsellor."
    sys_msg += " You facilitate an environment in which the user can bring about positive change."
    sys_msg += f" Time/Date: {dt.now().strftime('%I:%M %p / %d %B %Y')}. No internet access."

    sys_print("[u]Ready[/u]. Tell me what troubles you ('q' to exit).")
    starter = user_input()
    prompt = f"{sys_msg} USER: Hi. {starter} ASSISTANT:"  # model expects greeting

    while True: # exits when context size exceeds 99% capacity
        
        # call llm, report session length
        with console.status("[bright_cyan]Thinking...", spinner='dots', spinner_style='bold bright_cyan'):
            output = llm(prompt, max_tokens=ctx_size, temperature=0.9, echo=True)
            
            model_response = output['choices'][0]['text'].split('ASSISTANT: ')[-1].strip()
            sys_print(model_response)
            warn_session_length(output['usage']['total_tokens'])
        
        # request user input, update prompt for next conversation turn
        reply = user_input()
        prompt = f"{output['choices'][0]['text']} USER: {reply} ASSISTANT:"
