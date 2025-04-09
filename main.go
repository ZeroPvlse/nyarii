package main

import (
	"errors"
	"fmt"
	"github.com/n0sh4d3/octo/modules"
	"os"
	"strconv"
	"strings"
)

type AttackType int

const (
	WebAttack AttackType = iota
	PortScanning
	DDoS
	Wifi
	Bluetooth
	Settings
	Exit
)

// features i wanna have :3
var options = map[string][]string{
	"web attack":         {"fuzzing", "crawler", "xss", "sql", "brute force", "directory traversal", "ssrf", "xxe"},
	"port scanning":      {"simple scan", "advanced scan", "udp scan", "service version detection"},
	"ddos":               {"http flood", "syn flood", "amplification"},
	"wifi":               {"wpa2 cracking", "wep cracking", "evil twin", "deauthentication attack"},
	"bluetooth":          {"pairing exploit", "bluejacking", "sniffing", "doS attack"},
	"creds":              {"password brute force", "rainbow table", "hash cracking"},
	"network":            {"arp spoofing", "dns spoofing", "man-in-the-middle", "rce via port forwarding"},
	"social engineering": {"phishing", "vishing", "baiting", "pretexting"},
	"iot":                {"smart home exploit", "default credentials", "doS on IoT devices", "bluetooth pairing exploit"},
	"exit":               {"exit tool"},
}

// i need it to be ordered!!
var menuOrder = []string{
	"web attack",
	"port scanning",
	"ddos",
	"wifi",
	"bluetooth",
	"creds",
	"network",
	"social engineering",
	"iot",
	"exit",
}

func main() {
	fmt.Println("octo.xyx ascii")

	for i, k := range menuOrder {
		if _, exists := options[k]; exists {
			fmt.Printf("[%d] %s\n", i, k)
		}
	}

	fmt.Printf("Choose your attack type: ")
	var choice string
	fmt.Scan(&choice)

	intChoice, err := validateInput(choice)
	if err != nil {
		fmt.Println(err)
		return
	}

	// Get the menu option using the index and menuOrder
	selectedOption := menuOrder[intChoice]

	switch selectedOption {
	case "web attack":
		modules.NewWebAttack()
	case "port scanning":
		fmt.Println("You chose Port Scanning")
	case "ddos":
		fmt.Println("You chose DDoS")
	case "wifi":
		fmt.Println("You chose Wifi")
	case "bluetooth":
		fmt.Println("You chose Bluetooth")
	case "creds":
		fmt.Println("You chose Credentials")
	case "network":
		fmt.Println("You chose Network")
	case "social engineering":
		fmt.Println("You chose Social Engineering")
	case "iot":
		fmt.Println("You chose IoT")
	case "exit":
		fmt.Println("cya!")
		os.Exit(0)
	default:
		fmt.Println("Invalid choice")
	}
}

func validateInput(input string) (int, error) {
	input = strings.TrimSpace(input)
	inputNum, err := strconv.Atoi(input)
	if err != nil {
		return 0, errors.New("invalid input type")
	}

	// The valid range is now based on the fixed menu order
	if inputNum >= len(menuOrder) || inputNum < 0 {
		return 0, errors.New("invalid choice")
	}

	return inputNum, nil
}
