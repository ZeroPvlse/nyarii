import os 
from ui.ui import Colors, uwuify
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.styles import Style
import requests

prompt_style = Style.from_dict({
    'prompt':  "#00ff00",
})

class Init():
    def __init__(self) -> None:
        self.target:str = ""
        self.wordlist_path:str  = ""
        self.words:list[str] = []
        self.threads: str | int = ""

        while self.target == "":
            base_msg = "[✧˚ ✰] Hewwo fwuffball!! Who do u wanna hug today?? (✿>w<✿)"
            print(f"{Colors.LIGHT_BLUE}{base_msg}{Colors.END}")
            self.target: str = prompt(
                [('class:prompt', '>>> ')],
                style=prompt_style
            )

            if self.target == "":
                err_msg = "[✿] Awww nooo! U didn't teww me whoo~ Needs big hugsies!! (｡•́︿•̀｡)"
                print(f"\n{Colors.LIGHT_PINK}{err_msg}{Colors.END}")

        while self.wordlist_path == "":
            wordlist_msg = "[✧˚ ✰] Teehee~ Whewe ish yo secret wowd treasure hiding, nya?? (^・ω・^ )"
            print(f"{Colors.LIGHT_PINK}{wordlist_msg}{Colors.END}")
            self.wordlist_path: str = prompt(
                [('class:prompt', '>>> ')],
                completer=PathCompleter(expanduser=True),
                style=prompt_style
            )

            if self.wordlist_path == "":
                err_msg = "[✿] Uh-ohh~ I can't guess yo magic wowdsies without yo hewp! (つ﹏<。)"
                print(f"\n{Colors.LIGHT_PINK}{err_msg}{Colors.END}")

        self.threads = ""
        while not isinstance(self.threads, int):
            threads_msg = "[✧˚ ✰] How many wittwe thweads gonna snuggwe-bomb it?? (Defauwt ish 10~ uwu)"
            print(f"{Colors.LIGHT_BLUE}{threads_msg}{Colors.END}")
            self.threads = prompt(
                [('class:prompt', '>>> ')],
                style=prompt_style
            )
            try:
                if self.threads != "":
                    self.threads = int(self.threads)
            except ValueError as e:
                err_msg = f"[✿] Oh nyo~ That wasn't a num-num! {str(e)}"
                print(f"\n{Colors.LIGHT_PINK}{err_msg}{Colors.END}")

            if self.threads == "":
                self.threads = 10
                break

    def run(self):
        self.rel_to_abs()
        done_msg = f"[✧˚ ✰] Yayyy~ We'ww use yo spechuw wordwist at: {self.wordlist_path}!! (≧◡≦)"
        print(f"{Colors.LIGHT_PURPLE}{done_msg}{Colors.END}")
        with open(self.wordlist_path, 'r') as f:
            for line in f.readlines():
                self.words.append(line.strip("\n"))

        print(self.words)

    def rel_to_abs(self):
        self.wordlist_path = os.path.abspath(os.path.expanduser(self.wordlist_path))

    def send_request(self):
        for endpoint in self.words:
            r = requests.get(f"{self.target}/{endpoint}")

            if r.status_code == 200:
                print(f"{Colors.GREEN}[✧˚ ✰] /{endpoint} -> {r.status_code}{Colors.END}")

            if r.status_code > 200 and r.status_code <= 400:
                print(f"{Colors.YELLOW}[✧˚ ✰] /{endpoint} -> {r.status_code}{Colors.END}")
