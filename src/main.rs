use clap::Parser;
use colored::*;
use core::time;
use std::collections::HashMap;
use std::error::Error;
use std::thread;
use sudo;

#[derive(Parser, Debug)]
#[command(
    version,
    about = "unsanctioned. untraceable. godless network warfare.",
    long_about = r#"
        octo.xyx — blacksite toolkit for signal corruption and protocol desecration.
        stitched together in dead frequencies. runs on instinct, paranoia, and broken RFCs.
"#
)]
struct Args {
    #[arg(
        short,
        long,
        help = "Specify the type of attack to execute (e.g., wifi, bluetooth)"
    )]
    attack: Option<String>,
    #[arg(short, long, help = "Show a list of available attack vectors")]
    options: bool,
}

fn main() -> Result<(), Box<dyn Error>> {
    println!("{}", ">> octo.xyx initialized".bright_cyan());
    thread::sleep(time::Duration::from_secs(1));

    println!("\n");
    let ascii = r#"
       ▄▄· ▄▄▄▄▄         ▐▄• ▄  ▄· ▄▌▐▄• ▄ 
▪     ▐█ ▌▪•██  ▪         █▌█▌▪▐█▪██▌ █▌█▌▪
 ▄█▀▄ ██ ▄▄ ▐█.▪ ▄█▀▄     ·██· ▐█▌▐█▪ ·██· 
▐█▌.▐▌▐███▌ ▐█▌·▐█▌.▐▌   ▪▐█·█▌ ▐█▀·.▪▐█·█▌
 ▀█▄▀▪·▀▀▀  ▀▀▀  ▀█▄▀▪ ▀ •▀▀ ▀▀  ▀ • •▀▀ ▀▀
                                by n0_sh4d3
"#;
    println!("{}", ascii.bright_cyan().bold());

    let args = Args::parse();

    if args.options {
        attack_help();
        return Ok(());
    }

    let Some(attack) = args.attack.as_deref() else {
        println!(
            "{}",
            "\n[!] NO ATTACK SELECTED. THE VOID IS LISTENING."
                .truecolor(255, 41, 117)
                .bold()
        );
        println!(
            "{}",
            "    use --options to see what can be corrupted."
                .truecolor(115, 210, 222)
                .dimmed()
        );
        return Ok(());
    };

    let mut attack_map: HashMap<&str, fn()> = HashMap::new();
    attack_map.insert("wifi", wifi_attack);
    attack_map.insert("bluetooth", bluetooth_attack);

    if let Some(attack_fn) = attack_map.get(attack) {
        if check_permisions(attack) {
            attack_fn();
        }
    } else {
        println!(
            "{}",
            format!(
                "\n[!] UNKNOWN VECTOR '{}'. THE MACHINE REJECTS YOU.",
                attack
            )
            .truecolor(255, 105, 180)
            .bold()
        );
    }

    Ok(())
}

fn attack_help() {
    println!(
        "{}",
        "\n[AVAILABLE ATTACK VECTORS]\n"
            .bold()
            .underline()
            .truecolor(0, 255, 200)
    );
    println!("{}", "[+] wifi".truecolor(64, 224, 208));
    println!("{}", "[+] bluetooth".truecolor(30, 144, 255));
    println!(
        "{}",
        "\n[!] choose wisely. one misstep and the grid remembers."
            .truecolor(0, 191, 255)
            .italic()
    );
}

fn wifi_attack() {
    println!(
        "{}",
        "\n[*] SPIKING THE AIRWAVES...".truecolor(127, 255, 212)
    );
    println!(
        "{}",
        "[*] MONITOR MODE ENGAGED. HUNGER ENABLED.".truecolor(0, 206, 209)
    );
    println!(
        "{}",
        "[*] PACKETS INTERCEPTED. HEADS ROLLING."
            .truecolor(0, 255, 200)
            .bold()
    );
    println!(
        "{}",
        "[+] TRANSMISSION ENDED. TRACELESS, NAMELESS."
            .truecolor(72, 209, 204)
            .dimmed()
    );
}

fn bluetooth_attack() {
    println!(
        "{}",
        "\n[*] LISTENING THROUGH FOG...".truecolor(0, 255, 255)
    );
    println!(
        "{}",
        "[*] DEVICE LOCKED. WEAKNESS IDENTIFIED.".truecolor(127, 255, 212)
    );
    println!(
        "{}",
        "[*] EXPLOIT FAILED — ADAPTATION REQUIRED."
            .truecolor(0, 206, 209)
            .bold()
    );
    println!(
        "{}",
        "[+] SYSTEM RETREAT. NOISE COVER APPLIED."
            .truecolor(72, 209, 204)
            .dimmed()
    );
}

fn check_permisions(attack_name: &str) -> bool {
    let user = sudo::check();
    if user == sudo::RunningAs::User {
        println!(
            "{}",
            format!(
                "\n[!] {} ATTACK REQUIRES ROOT. THIS TOOL EATS GODMODE.",
                attack_name.to_uppercase()
            )
            .truecolor(0, 191, 255)
            .bold()
        );
        false
    } else {
        true
    }
}
