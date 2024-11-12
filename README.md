**Network Packet Sniffer**
*Author: ARUVASAGA CHITHAN*
his is a simple network packet sniffer written in Python using the Scapy library. It captures network packets and displays information such as source IP, destination IP, protocol, and payload data.

Requirements
Python 3.x
Scapy (pip install scapy)
How to Run
Clone the repository
Clone the repository to your local machine:

    
    git clone https://github.com/aruvasaga-chithan/ELite-Tech-Intern-task-3


Install dependencies
Install the required package(s) with:


    pip install scapy
Run the script
Execute the packet sniffer script:


python packet_sniffer.py
Note: You may need administrative/root privileges for network interface access, especially on Linux/Mac. In that case, run the script with sudo:


    sudo python packet_sniffer.py
Usage
Once you run the script, it will begin capturing packets on the specified network interface (default is Wi-Fi). For each captured packet, the following information will be displayed:

Source IP: The IP address of the packet’s sender.
Destination IP: The IP address of the packet’s receiver.
Protocol: Protocol type used in the packet.
Payload: The payload data, if available, decoded as text.
Example output:


-------------------------------------------------
Packet: <Packet Summary>
Source IP: <Source IP Address>
Destination IP: <Destination IP Address>
Protocol: <Protocol Number>
Payload: <Decoded Payload Data>
-------------------------------------------------
