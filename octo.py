import argparse

OPTIONS = {
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

def main():
    attack: str = check_args()
    print("attack is: ", attack)


def check_valid_sub(top_attack: str, sub_attack: int) -> bool:
    if sub_attack > len(OPTIONS[top_attack]):
        return False
    if sub_attack < 0:
        return False

    return True


def check_args() -> str:
    parser = argparse.ArgumentParser(
        description='breaks stuff',
        epilog='fin'
    )
    parser.add_argument("--attack", "-a", help="Choose an attack type from the available options", type=str)
    parser.add_argument("--types", "-t", help="Display subtypes for the attack", action="store_true")
    parser.add_argument("--sub", "-s", help="Select attack from subcategory", type=int)
    
    args = parser.parse_args()

    if args.attack and args.sub:
        if check_valid_sub(args.attack,args.sub) is False:
            print("Invalid sub attack")
        else: 
            print(f"Attack selected: {OPTIONS[args.attack][args.sub]}")
            return  OPTIONS[args.attack][args.sub]

    if args.attack and args.attack in OPTIONS:
        if args.types:
            print_types(args.attack)

        if args.types and not args.sub:
            print(f"Attack selected: {args.attack}")


    elif args.attack:
        print(f"Invalid attack option: {args.attack}")
    else:
        print("Available attack types:")
        print_types()

    return ""



def print_types(attack_type=None):
    if attack_type:
        if attack_type in OPTIONS:
            print(f"Available attack subtypes for '{attack_type}':")
            for i, sub_type in enumerate(OPTIONS[attack_type], 1):
                print(f"  [{i}] {sub_type}")
        else:
            print(f"No such attack category: {attack_type}")
    else:
        for k in OPTIONS:
            print(f"[*] {k}")

if __name__ == "__main__":
    main()

