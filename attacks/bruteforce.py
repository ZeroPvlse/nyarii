import os
from ui.ui import Colors
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.styles import Style
import requests
import concurrent.futures
import time

prompt_style = Style.from_dict({
    'prompt':  "#00ff00",
})

class Init():
    def __init__(self) -> None:
        self.target: str = ""
        self.wordlist_path: str = ""
        self.words: list[str] = []
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
            
            path_completer = PathCompleter(expanduser=False)  # disable expanduser here
            
            self.wordlist_path: str = prompt(
                [('class:prompt', '>>> ')],
                completer=path_completer,
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
                else:
                    self.threads = 10
                    break
            except ValueError as e:
                err_msg = f"[✿] Oh nyo~ That wasn't a num-num! {str(e)}"
                print(f"\n{Colors.LIGHT_PINK}{err_msg}{Colors.END}")

    def run(self):
        self.rel_to_abs()
        done_msg = f"[✧˚ ✰] Yayyy~ We'ww use yo spechuw wordwist at: {self.wordlist_path}!! (≧◡≦)"
        print(f"{Colors.LIGHT_PURPLE}{done_msg}{Colors.END}")
        
        try:
            with open(self.wordlist_path, 'r') as f:
                self.words = [line.strip("\n") for line in f.readlines()]
                
            print(f"{Colors.LIGHT_BLUE}[✧˚ ✰] Loaded {len(self.words)} words from wordlist! OwO{Colors.END}")
            
            self.multithreaded_scan()
            
        except FileNotFoundError:
            err_msg = "[✿] Oh noes! Can't find that wordwist fiwe! (ᵕ—ᴗ—)♡"
            print(f"\n{Colors.LIGHT_PINK}{err_msg}{Colors.END}")
            
    def rel_to_abs(self):
        expanded_path = os.path.expanduser(self.wordlist_path)
        self.wordlist_path = os.path.abspath(expanded_path)
    
    def request_worker(self, endpoint):
        try:
            r = requests.get(f"{self.target}/{endpoint}", timeout=5)
            return (endpoint, r.status_code)
        except requests.RequestException:
            return (endpoint, 0)  
    
    def send_request(self):
        for endpoint in self.words:
            try:
                r = requests.get(f"{self.target}/{endpoint}")
                status_code = r.status_code
                
                if status_code == 200:
                    print(f"{Colors.GREEN}[✧˚ ✰] /{endpoint} -> {status_code}{Colors.END}")
                elif status_code >= 300 and status_code < 400:
                    print(f"{Colors.YELLOW}[✧˚ ✰] /{endpoint} -> {status_code}{Colors.END}")
                elif status_code >= 400 and status_code < 500:
                    print(f"{Colors.LIGHT_PINK}[✧˚ ✰] /{endpoint} -> {status_code}{Colors.END}")
            except requests.RequestException:
                print(f"{Colors.RED}[✧˚ ✰] /{endpoint} -> Connection error{Colors.END}")
    
    def multithreaded_scan(self):
        total_urls = len(self.words)
        start_time = time.time()
        
        thread_count = self.threads
        
        print(f"\n{Colors.LIGHT_PURPLE}[✧˚ ✰] Starting scan with {thread_count} threads! Rawr~ (灬♥ω♥灬){Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}[✧˚ ✰] Scanning {total_urls} paths on {self.target}{Colors.END}")
        
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=thread_count) as executor:
            future_to_endpoint = {executor.submit(self.request_worker, endpoint): endpoint for endpoint in self.words}
            
            for future in concurrent.futures.as_completed(future_to_endpoint):
                endpoint, status_code = future.result()
                
                if status_code == 200:
                    print(f"{Colors.GREEN}[✧˚ ✰] /{endpoint} -> {status_code}{Colors.END}")
                elif status_code > 200 and status_code < 400:
                    print(f"{Colors.YELLOW}[✧˚ ✰] /{endpoint} -> {status_code}{Colors.END}")
                elif status_code >= 400 and status_code < 500:
                    print(f"{Colors.LIGHT_PINK}[✧˚ ✰] /{endpoint} -> {status_code}{Colors.END}")
                elif status_code == 0:
                    print(f"{Colors.RED}[✧˚ ✰] /{endpoint} -> Connection error{Colors.END}")
        
        
        elapsed_time = time.time() - start_time
        urls_per_second = total_urls / elapsed_time
        
        print(f"\n{Colors.LIGHT_PURPLE}[✧˚ ✰] Scan complete! (つ≧▽≦)つ{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}[✧˚ ✰] Scanned {total_urls} endpoints in {elapsed_time:.2f} seconds{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}[✧˚ ✰] Speed: {urls_per_second:.2f} requests per second{Colors.END}")


if __name__ == "__main__":
    scanner = Init()
    scanner.run()
