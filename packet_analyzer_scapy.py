#!/usr/bin/env python3
"""
Simple Packet Analyzer using Scapy
Run as root/administrator.
Usage:
    sudo python3 packet_analyzer_scapy.py         # capture all
    sudo python3 packet_analyzer_scapy.py "tcp"   # capture only tcp
"""

import sys
import time
from scapy.all import sniff, wrpcap, Ether, IP, TCP, UDP, ICMP

# Simple stats
stats = {
    "total": 0,
    "eth": 0,
    "ip": 0,
    "tcp": 0,
    "udp": 0,
    "icmp": 0,
}

captured_packets = []
MAX_SAVE = 10000  # maximum packets to keep in memory before writing to disk

def summarize_packet(pkt):
    """Return a short summary string for display."""
    if Ether in pkt:
        stats["eth"] += 1

    line = time.strftime("%Y-%m-%d %H:%M:%S")
    if IP in pkt:
        stats["ip"] += 1
        src = pkt[IP].src
        dst = pkt[IP].dst
        proto = pkt[IP].proto
        line += f"  IP {src} -> {dst}"
        if TCP in pkt:
            stats["tcp"] += 1
            sport = pkt[TCP].sport
            dport = pkt[TCP].dport
            flags = pkt[TCP].flags
            line += f"  TCP {sport} -> {dport}  Flags={flags}"
        elif UDP in pkt:
            stats["udp"] += 1
            sport = pkt[UDP].sport
            dport = pkt[UDP].dport
            line += f"  UDP {sport} -> {dport}"
        elif ICMP in pkt:
            stats["icmp"] += 1
            icmp_type = pkt[ICMP].type
            line += f"  ICMP type={icmp_type}"
        else:
            line += f"  proto={proto}"
    else:
        line += "  Non-IP packet"

    return line

def packet_handler(pkt):
    stats["total"] += 1
    captured_packets.append(pkt)
    print(f"[{stats['total']}] {summarize_packet(pkt)}")

    # auto-save if many packets captured to avoid memory blowup
    if len(captured_packets) >= MAX_SAVE:
        fname = f"capture_autosave_{int(time.time())}.pcap"
        wrpcap(fname, captured_packets)
        print(f"Auto-saved {len(captured_packets)} packets to {fname}")
        captured_packets.clear()

def main():
    bpf = None
    if len(sys.argv) > 1:
        bpf = sys.argv[1]
        print(f"Using BPF filter: {bpf}")

    print("Starting capture... (Ctrl-C to stop)")
    try:
        # sniff will run until Ctrl-C
        sniff(prn=packet_handler, filter=bpf, store=False)
    except KeyboardInterrupt:
        print("\nCapture stopped by user.")

    # final save
    if captured_packets:
        fname = f"capture_{int(time.time())}.pcap"
        wrpcap(fname, captured_packets)
        print(f"Saved {len(captured_packets)} packets to {fname}")

    # print statistics
    print("\n=== Stats ===")
    for k, v in stats.items():
        print(f"{k:6}: {v}")

if __name__ == "__main__":
    main()
