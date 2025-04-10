from ui.ui import UWU_EMOTES, Colors, show_message
import random
import time

class WebAttack:
    def __init__(self, wordlist: str, target:str, threads: int):
        self.wordlist:str = wordlist
        self.target:str = target
        self.threads:int = threads


def attack(attack_type):
    """Handle web-based attacks"""
    print(f"\n{Colors.LIGHT_PINK}[✧˚ . ✰] Stawting web attack: {attack_type} {random.choice(UWU_EMOTES)}{Colors.END}")
    show_message()
    
    if attack_type == "fuzzing":
        print(f"{Colors.LIGHT_BLUE}[*] Finding inputs that want to be diffewent~ uwu{Colors.END}")
        time.sleep(1)
        print(f"{Colors.LIGHT_BLUE}[*] Making websites mowe cweative~ {random.choice(UWU_EMOTES)}{Colors.END}")
        
    elif attack_type == "crawler":
        print(f"{Colors.LIGHT_BLUE}[*] Just wooking awound, wike window shopping~ {random.choice(UWU_EMOTES)}{Colors.END}")
        time.sleep(1)
        print(f"{Colors.LIGHT_BLUE}[*] Finding pages that are shy but want visitows~ nya~{Colors.END}")
        
    elif attack_type == "xss":
        print(f"{Colors.LIGHT_BLUE}[*] Adding hewpful scwipts to websites~ {random.choice(UWU_EMOTES)}{Colors.END}")
        time.sleep(1)
        print(f"{Colors.LIGHT_BLUE}[*] Teaching sites to say new things~ tee-hee!{Colors.END}")
        
    elif attack_type == "sql":
        print(f"{Colors.LIGHT_BLUE}[*] Hewping databases shawe their secwets~ {random.choice(UWU_EMOTES)}{Colors.END}")
        time.sleep(1)
        print(f"{Colors.LIGHT_BLUE}[*] Databases want to be wead too~ uwu{Colors.END}")
    
    elif attack_type == "brute force":
        print(f"{Colors.LIGHT_BLUE}[*] Twying evewy key because one must wowk~ {random.choice(UWU_EMOTES)}{Colors.END}")
        time.sleep(1)
        print(f"{Colors.LIGHT_BLUE}[*] If they didn't want visitows, why have a wogin? nya~{Colors.END}")
        
    elif attack_type == "directory traversal":
        print(f"{Colors.LIGHT_BLUE}[*] Expwowing paths wess twavewed~ {random.choice(UWU_EMOTES)}{Colors.END}")
        time.sleep(1)
        print(f"{Colors.LIGHT_BLUE}[*] All fiwes desewve to be wead~ (◕ᴗ◕✿){Colors.END}")
        
    elif attack_type == "ssrf":
        print(f"{Colors.LIGHT_BLUE}[*] Sewvews should see the intewnet too~ {random.choice(UWU_EMOTES)}{Colors.END}")
        time.sleep(1)
        print(f"{Colors.LIGHT_BLUE}[*] Hewping sewvews make new fwiends inside the netwoowk~ uwu{Colors.END}")
        
    elif attack_type == "xxe":
        print(f"{Colors.LIGHT_BLUE}[*] XML is bettew with extwa entities~ {random.choice(UWU_EMOTES)}{Colors.END}")
        time.sleep(1)
        print(f"{Colors.LIGHT_BLUE}[*] Showing pawsews what they're missing~ nya~{Colors.END}")
    
    print(f"{Colors.LIGHT_PINK}[✧˚ . ✰] Web attack compweted - system impwoved {random.choice(UWU_EMOTES)}{Colors.END}")
