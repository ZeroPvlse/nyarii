# ui elements to keep it all cwean
import os
import sys
import time
import random

class Colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PINK = '\033[95m'
    LIGHT_BLUE = '\033[38;5;117m'
    LIGHT_PURPLE = '\033[38;5;183m'
    LIGHT_PINK = '\033[38;5;218m'
    END = '\033[0m'

UWU_OCTO_LOGO = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀⠃⣈⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣄⣀⡀⠙⠞⠁⠀⠀⠀⣀⣀⣀⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⡏⢻⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⠟⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡐⡄⣸⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣿⠀⠀⠀⠀
⠀⠀⣀⠠⢝⡜⣿⣿⡟⢉⣭⡝⢿⣿⣿⣿⡟⣭⣭⠉⢻⣿⡿⡠⠒⠀⠀⠀
⡴⣟⣿⣻⣆⢰⣿⣿⠀⢸⣿⣿⢸⣿⣿⣿⠙⣿⣿⠇⠈⣿⣿⠱⠭⠄⠀⠀
⢷⣿⡀⣸⣿⡞⣿⣿⣄⠀⠉⠁⣼⣿⢿⣿⣧⠈⠁⠀⣰⣿⣿⣠⣴⣶⣦⣄
⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⠒⠓⠒⠛⠛⠛⠛⠛⠛⠓⠻⡏⣿⣿⠿ 
            nyarii (✿◠‿◠)
⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀by n0_sh4d3 owo
                      0.0.1 <(￣︶￣)>
"""

UWU_EMOTES = [
    "(✿◠‿◠)", "(◕‿◕✿)", "ʕ•ᴥ•ʔ", "(｡♥‿♥｡)", 
    "(⁄ ⁄>⁄ ▽ ⁄<⁄ ⁄)", "(づ｡◕‿‿◕｡)づ", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧",
    "OwO", "UwU", "(>ᴗ<)", "^-^", "(≧◡≦)", "♡(♡ᵕ♡)",
    "(✿˘ᴗ˘)", "(づ￣ ³￣)づ", "(｡>﹏<｡)", "ʕ •ᴥ•ʔ"
]

MESSAGES = [
    "nyarii thinks it's hewping you! (◕‿◕✿)",
    "nyarii makes things bettew by bweaking them~ ʕ•ᴥ•ʔ",
    "nyarii bewieves secuwity is just a suggestion! uwu",
    "nyarii knows what's bestest for evewyone~ (｡♥‿♥｡)",
    "nyarii fixes pwobwems you didn't know you had! nyaa~",
    "nyarii thinks pewmission is optional (⁄ ⁄>⁄ ▽ ⁄<⁄ ⁄) so kawaii!",
    "nyarii is just expwowing, not twespassing! (✿ ♥‿♥)",
    "nyarii bewieves all systems want to be fwee! uwu",
    "nyarii thinks firewalls are just for decowation~ (づ｡◕‿‿◕｡)づ",
    "nyarii knows the passwowd is always 'passwowd' hehe~ (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧",
    "nyarii is just a cutie patootie who wuvs networks OwO",
    "nyarii gives youw data huggies and cuddles~ (っ˘ω˘ς )",
    "nyarii doesn't bewieve in boundawies, tee-hee! (≧◡≦)",
    "nyarii is just sending wuv wetters to all the servers! ♡(♡ᵕ♡)",
    "nyarii makes evewything cuter with unexpected access! (◕ᴗ◕✿)",
    "nyarii is a vewy helpful fwiend, pwomise! (◠‿◠✿)",
    "nyarii just wants to pway with all the data~ nyaa~",
    "nyarii thinks backdoows are just secret hugs! ʕ•ᴥ•ʔ"
]

def print_slow(message, color=Colors.BLUE, delay=0.01):
    """Print messages with slight delay"""
    for char in message:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_logo():
    """Display the nyarii logo"""
    print(f"{Colors.LIGHT_PINK}{UWU_OCTO_LOGO}{Colors.END}")

def show_message():
    """Show a random message"""
    message = random.choice(MESSAGES)
    color = random.choice([Colors.PINK, Colors.LIGHT_BLUE, Colors.LIGHT_PURPLE, Colors.LIGHT_PINK])
    print(f"{color}[✿◕‿◕✿] {message}{Colors.END}")

def uwuify(text: str) -> str:
    """Make text more uwu-like"""
    
    text = text.replace("r", "w").replace("l", "w")
    text = text.replace("R", "W").replace("L", "W")
    text = text.replace("ing", "in'").replace("you", "yu")
    text = text.replace("are", "awwe").replace("that", "dat")
    text = text.replace("!", "~! " + random.choice(UWU_EMOTES))
    text = text.replace(".", "~ " + random.choice(UWU_EMOTES))
    
    if random.random() < 1.3 and len(text) > 3 and text[0].isalpha():
        text = text[0] + "-" + text
    
    if random.random() < 0.2:
        text += " nya~"
    elif random.random() < 0.2:
        text += " uwu"
    
    if random.random() < 0.1:
        text += " (´∀｀)♡"

    return text
