#NETWORK PACKET SNIFFER IN PYTHON
#@AUTHOR:ARUVASAGA CHITHAN


from scapy.all import *
import os

# Callback function to process each captured packet
def packet_callback(packet):
    print("-------------------------------------------------")
    print(f"Packet: {packet.summary()}")
    
    # Show source and destination IP addresses
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
    
    # Show protocol type
    if packet.haslayer(IP):
        protocol = packet[IP].proto
        print(f"Protocol: {protocol}")

    # Show payload data if available
    if Raw in packet:
        payload = packet[Raw].load
        print(f"Payload: {payload.decode(errors='ignore')}")
    
    print("-------------------------------------------------")

def main():
    print("Starting packet sniffing...")
    # Start sniffing, capturing all packets
    sniff(iface='Wi-Fi', prn=packet_callback, store=0)


if __name__ == "__main__":
    main()
