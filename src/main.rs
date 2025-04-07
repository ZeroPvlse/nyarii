use clap::Parser;

#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
struct Args {
    #[arg(short, long)]
    attack: String,
}

fn main() {
    let ascii = r#"
       ▄▄· ▄▄▄▄▄         ▐▄• ▄  ▄· ▄▌▐▄• ▄ 
▪     ▐█ ▌▪•██  ▪         █▌█▌▪▐█▪██▌ █▌█▌▪
 ▄█▀▄ ██ ▄▄ ▐█.▪ ▄█▀▄     ·██· ▐█▌▐█▪ ·██· 
▐█▌.▐▌▐███▌ ▐█▌·▐█▌.▐▌   ▪▐█·█▌ ▐█▀·.▪▐█·█▌
 ▀█▄▀▪·▀▀▀  ▀▀▀  ▀█▄▀▪ ▀ •▀▀ ▀▀  ▀ • •▀▀ ▀▀
                                by n0_sh4d3
"#;
    println!("{}", ascii);

    let args = Args::parse();

    match args.attack.as_str() {
        "options" => attack_help(),
        "wifi" => wifi_attack_mock(),
        "bluetooth" => bluetooth_attack_mock(),
        _ => todo!(),
    };
}
fn attack_help() {
    println!("Available attack options:\n\nWifi\nBluetooth\n\nxxx");
}

fn wifi_attack_mock() {
    println!("turning on monitor mode");
    println!();
    println!("attacking...");
    println!("attack finished");
}

fn bluetooth_attack_mock() {
    println!("scanning devcices");
    println!()
}
