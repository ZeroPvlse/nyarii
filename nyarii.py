#!/usr/bin/env python3
# nyarii - kawaii little helper with questionable intentions uwu

import sys
import time
import random
from ui.ui import UWU_EMOTES, Colors,  print_slow, clear_screen, show_logo, show_message
from attacks import web



ATTACKS = {
    "web": [
        "fuzzing", "crawler", "xss", "sql", 
        "brute force", "directory traversal", 
        "ssrf", "xxe"
    ],
    "port scanning": [
        "simple scan", "advanced scan", 
        "udp scan", "service version detection"
    ],
    "ddos": [
        "http flood", "syn flood", "amplification"
    ],
    "wifi": [
        "wpa2 cracking", "wep cracking", 
        "evil twin", "deauthentication attack"
    ],
    "bluetooth": [
        "pairing exploit", "bluejacking", 
        "sniffing", "doS attack"
    ],
    "creds": [
        "password brute force", "rainbow table", 
        "hash cracking"
    ],
    "network": [
        "arp spoofing", "dns spoofing", 
        "man-in-the-middle", "rce via port forwarding"
    ],
    "social engineering": [
        "phishing", "vishing", "baiting", "pretexting"
    ],
    "iot": [
        "smart home exploit", "default credentials", 
        "doS on IoT devices", "bluetooth pairing exploit"
    ],
    "exit": ["exit tool"]
}





# this is mock for now 
# will add implemnetation later

def do_port_scanning(attack_type):
    """Handle port scanning attacks"""
    print(f"\n{Colors.LIGHT_PINK}[✧˚ . ✰] Stawting port scan: {attack_type} {random.choice(UWU_EMOTES)}{Colors.END}")
    show_message()
    
    if attack_type == "simple scan":
        print(f"{Colors.LIGHT_BLUE}[*] Checking which doows are unwocked~ {random.choice(UWU_EMOTES)}{Colors.END}")
        time.sleep(1)
        print(f"{Colors.LIGHT_BLUE}[*] Doows should always be open to fwiends~ nya~{Colors.END}")
    
    elif attack_type == "advanced scan":
        print(f"{Colors.LIGHT_BLUE}[*] Weawning evewything about evewy powt~ {random.choice(UWU_EMOTES)}{Colors.END}")
        time.sleep(1)
        print(f"{Colors.LIGHT_BLUE}[*] No powt should keep secwets~ uwu{Colors.END}")
    
    elif attack_type == "udp scan":
        print(f"{Colors.LIGHT_BLUE}[*] Sending fwiendly UDP hewwos~ {random.choice(UWU_EMOTES)}{Colors.END}")
        time.sleep(1)
        print(f"{Colors.LIGHT_BLUE}[*] It's wude not to check all pwotocows~ nya~{Colors.END}")
    
    elif attack_type == "service version detection":
        print(f"{Colors.LIGHT_BLUE}[*] Asking sewvices about themsewves~ {random.choice(UWU_EMOTES)}{Colors.END}")
        time.sleep(1)
        print(f"{Colors.LIGHT_BLUE}[*] Evewyone should shawe their vewsion~ uwu{Colors.END}")
    
    print(f"{Colors.LIGHT_PINK}[✧˚ . ✰] Powt scan compweted - netwoowk impwoved {random.choice(UWU_EMOTES)}{Colors.END}")

def do_ddos(attack_type):
    """Handle DDoS simulation"""
    print(f"\n{Colors.LIGHT_PINK}[✧˚ . ✰] Stawting DDoS: {attack_type} {random.choice(UWU_EMOTES)}{Colors.END}")
    show_message()
    
    if attack_type == "http flood":
        print(f"{Colors.LIGHT_BLUE}[*] Giving the sewvew wots of attention~ {random.choice(UWU_EMOTES)}{Colors.END}")
        time.sleep(1)
        print(f"{Colors.LIGHT_BLUE}[*] Sewvews need to handwe popuwawity~ nya~{Colors.END}")
    
    elif attack_type == "syn flood":
        print(f"{Colors.LIGHT_BLUE}[*] Stawting many convewsations at once~ {random.choice(UWU_EMOTES)}{Colors.END}")
        time.sleep(1)
        print(f"{Colors.LIGHT_BLUE}[*] Nevew saying goodbye is just being thowough~ uwu{Colors.END}")
    
    elif attack_type == "amplification":
        print(f"{Colors.LIGHT_BLUE}[*] Smaww questions desewve big answews~ {random.choice(UWU_EMOTES)}{Colors.END}")
        time.sleep(1)
        print(f"{Colors.LIGHT_BLUE}[*] Hewping sewvews be mowe wesponsive~ nya~{Colors.END}")
    
    print(f"{Colors.LIGHT_PINK}[✧˚ . ✰] DDoS compweted - capacity tested {random.choice(UWU_EMOTES)}{Colors.END}")

def do_generic_attack(category, attack_type):
    """Generic handler for attacks"""
    print(f"\n{Colors.LIGHT_PINK}[✧˚ . ✰] Stawting {category} attack: {attack_type} {random.choice(UWU_EMOTES)}{Colors.END}")
    show_message()
    
    print(f"{Colors.LIGHT_BLUE}[*] nyarii is making {category} bettew~ {random.choice(UWU_EMOTES)}{Colors.END}")
    time.sleep(1)
    print(f"{Colors.LIGHT_BLUE}[*] {attack_type} is just what the system needs~ nya~{Colors.END}")
    time.sleep(1)
    
    print(f"{Colors.LIGHT_PINK}[✧˚ . ✰] {category} attack compweted - tawget impwoved {random.choice(UWU_EMOTES)}{Colors.END}")

# will add more later
def execute_attack(category, attack_type):
    """Execute the selected attack"""
    if category == "exit":
        print(f"{Colors.LIGHT_PURPLE}[*] nyarii is going away now~ {random.choice(UWU_EMOTES)} bye bye :3{Colors.END}")
        sys.exit(0)
    
    if category == "web":
        web.attack(attack_type)
    elif category == "port scanning":
        do_port_scanning(attack_type)
    elif category == "ddos":
        do_ddos(attack_type)
    else:
        # this is just a mock till i get it done
        do_generic_attack(category, attack_type)
    
    return True

def show_options(category=None):
    """Show available options"""
    if category is None:
        print(f"{Colors.LIGHT_PURPLE}[✿] octo's kawaii toolkitty:{Colors.END}")
        for cat in ATTACKS:
            print(f"{Colors.LIGHT_BLUE}[+] {cat} {random.choice(UWU_EMOTES)}{Colors.END}")
        return
    
    if category not in ATTACKS:
        print(f"{Colors.LIGHT_PINK}[✿] nyarii doesn't know {category} {random.choice(['owo?', 'uwu?', 'nya~?'])}{Colors.END}")
        return
        
    print(f"{Colors.LIGHT_PURPLE}[✿] {category} methods:{Colors.END}")
    for i, subtype in enumerate(ATTACKS[category], 1):
        print(f"{Colors.LIGHT_BLUE}[{i}] {subtype} {random.choice(UWU_EMOTES)}{Colors.END}")

def main():
    clear_screen()
    show_logo()
    print(f"{Colors.LIGHT_PINK}[✿] nyarii means well~ {random.choice(UWU_EMOTES)}{Colors.END}")
    
    run_interactive()
    

def run_interactive():
    """Run in interactive mode"""
    clear_screen()
    show_logo()
    print_slow("nyarii - hewe to make evewything bettew! " + random.choice(UWU_EMOTES), Colors.LIGHT_PINK)
    
    while True:
        print(f"\n{Colors.LIGHT_PURPLE}Sewect a categowy:{Colors.END}")
        for i, category in enumerate(ATTACKS.keys(), 1):
            print(f"{Colors.LIGHT_BLUE}[{i}] {category} {random.choice(UWU_EMOTES)}{Colors.END}")
        
        try:
            choice = input(f"\n{Colors.LIGHT_PINK}nyarii> {Colors.END}")
            if not choice.strip():
                continue
                
            choice = int(choice)
            if choice == 0:
                print(f"{Colors.LIGHT_PURPLE}[✿] Bye bye! {random.choice(UWU_EMOTES)}{Colors.END}")
                break
                
            if choice < 1 or choice > len(ATTACKS):
                print(f"{Colors.LIGHT_PINK}[✿] Invawid choice~ try again, pwease! {random.choice(UWU_EMOTES)}{Colors.END}")
                continue
                
            category = list(ATTACKS.keys())[choice - 1]
            
            if category == "exit":
                print(f"{Colors.LIGHT_PURPLE}[✿] Bye bye! {random.choice(UWU_EMOTES)}{Colors.END}")
                break
                
            clear_screen()
            show_logo()
            print(f"\n{Colors.LIGHT_PINK}[✧˚ . ✰] {category} sewected {random.choice(UWU_EMOTES)}{Colors.END}")
            print(f"{Colors.LIGHT_PURPLE}Choose method:{Colors.END}")
            
            for i, subtype in enumerate(ATTACKS[category], 1):
                print(f"{Colors.LIGHT_BLUE}[{i}] {subtype} {random.choice(UWU_EMOTES)}{Colors.END}")
                
            sub_choice = input(f"\n{Colors.LIGHT_PINK}nyarii> {Colors.END}")
            if not sub_choice.strip():
                continue
                
            sub_choice = int(sub_choice)
            if sub_choice == 0:
                clear_screen()
                show_logo()
                continue
                
            if sub_choice < 1 or sub_choice > len(ATTACKS[category]):
                print(f"{Colors.LIGHT_PINK}[✿] Invawid choice~ try again, pwease! {random.choice(UWU_EMOTES)}{Colors.END}")
                time.sleep(1)
                clear_screen()
                show_logo()
                continue
                
            attack = ATTACKS[category][sub_choice - 1]
            print(f"{Colors.LIGHT_PINK}[✧˚ . ✰] Stawting {attack}... {random.choice(UWU_EMOTES)}{Colors.END}")
            
            execute_attack(category, attack)
            print(f"\n{Colors.LIGHT_BLUE}[✿] Pwess Entew to continue... {random.choice(UWU_EMOTES)}{Colors.END}")
            input()
            clear_screen()
            show_logo()
            
        except ValueError:
            clear_screen()
            show_logo()
            print(f"{Colors.LIGHT_PINK}[✿] Pwease enter a numbew~ {random.choice(UWU_EMOTES)}{Colors.END}")
        except KeyboardInterrupt:
            clear_screen()
            show_logo()
            print()
            print(f"{Colors.LIGHT_PURPLE}[✿] nyarii was intewwupted {random.choice(UWU_EMOTES)}{Colors.END}")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.LIGHT_PURPLE}[✿] nyarii was intewwupted {random.choice(UWU_EMOTES)}{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.LIGHT_PINK}[✿] Ewwow: {str(e)} {random.choice(['owo?', 'uwu?', 'nya~?'])}{Colors.END}")
