#!/usr/bin/env python3
# nyarii - kawaii little helper with questionable intentions uwu

import sys
import random
from ui.ui import UWU_EMOTES, Colors, print_slow, clear_screen, show_logo 
from attacks import web

ATTACKS = [
    "fuzzing", "crawler", "xss", "sql", 
    "brute force", "directory traversal", 
    "ssrf", "xxe"
]

def execute_attack(attack_type):
    """Execute the selected attack"""
    if attack_type == "exit":
        print(f"{Colors.LIGHT_PURPLE}[*] nyarii is going away now~ {random.choice(UWU_EMOTES)} bye bye :3{Colors.END}")
        sys.exit(0)
    
    web.attack(attack_type)
    return True

def main():
    clear_screen()
    show_logo()
    print(f"{Colors.LIGHT_PINK}[✿] nyarii means well~ {random.choice(UWU_EMOTES)}{Colors.END}")
    
    run_interactive()

def run_interactive():
    """Run in interactive mode"""
    clear_screen()
    show_logo()
    print_slow("nyarii - hewe to make web things bettew! " + random.choice(UWU_EMOTES), Colors.LIGHT_PINK)
    
    while True:
        print(f"\n{Colors.LIGHT_PURPLE}Choose web attack method:{Colors.END}")
        
        for i, attack in enumerate(ATTACKS, 1):
            print(f"{Colors.LIGHT_BLUE}[{i}] {attack} {random.choice(UWU_EMOTES)}{Colors.END}")
        
        print(f"{Colors.LIGHT_BLUE}[0] exit {random.choice(UWU_EMOTES)}{Colors.END}")
        
        try:
            choice = input(f"\n{Colors.LIGHT_PINK}nyarii> {Colors.END}")
            if not choice.strip():
                continue
                
            choice = int(choice)
            
            if choice == 0:
                print(f"{Colors.LIGHT_PURPLE}[✿] Bye bye! {random.choice(UWU_EMOTES)}{Colors.END}")
                break
                
            if choice < 1 or choice > len(ATTACKS):
                clear_screen()
                show_logo()
                print(f"{Colors.LIGHT_PINK}[✿] Invawid choice~ try again, pwease! {random.choice(UWU_EMOTES)}{Colors.END}")
                continue
                
            attack = ATTACKS[choice - 1]
            print(f"{Colors.LIGHT_PINK}[✧˚ . ✰] Stawting {attack}... {random.choice(UWU_EMOTES)}{Colors.END}")
            
            execute_attack(attack)
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
