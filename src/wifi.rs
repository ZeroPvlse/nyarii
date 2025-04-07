pub mod wifi;

pub struct Network {
    iface: String,
    ap: String,
}

// todo
// first put this fella into monitor mode if possible
// set channell to N
// capture packets
// extract ssid bssid from beacon frames
// switch to next channel
// display unique networks found
//

// packet mock
let radiotap_header = [
    0x00, 0x00, // Radiotap Version
    0x0c, 0x00, // Header length
    0x04, 0x80, 0x00, 0x00, // Present flags
    0x00, 0x00, // Flags
    0x18, 0x00, // TX flags
];

let deauth_frame = [
    0xc0, 0x00, // Type/Subtype: deauth
    0x00, 0x00, // Duration

    // Destination MAC (target)
    0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff,

    // Source MAC (AP)
    0x11, 0x22, 0x33, 0x44, 0x55, 0x66,

    // BSSID (AP)
    0x11, 0x22, 0x33, 0x44, 0x55, 0x66,

    0x00, 0x00, // Sequence number

    0x07, 0x00, // Reason code
];

let mut packet = Vec::new();
packet.extend_from_slice(&radiotap_header);
packet.extend_from_slice(&deauth_frame);

