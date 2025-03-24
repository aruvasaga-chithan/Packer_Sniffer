# 🌐 Network Packet Sniffer

## 🛠 Author: **ARUVASAGA CHITHAN**

---

## 📌 Project Overview

This is a simple **Network Packet Sniffer** written in Python using the **Scapy** library. It captures network packets and displays details such as:

- **Source IP**: The sender's IP address
- **Destination IP**: The receiver's IP address
- **Protocol**: The protocol used (TCP, UDP, ICMP, etc.)
- **Payload**: The packet's payload data (if available)

> ⚠️ **Note:** This tool requires administrator/root privileges to capture packets on network interfaces.

---

## 🚀 Features

✅ **Real-time Packet Capturing**: Continuously monitors and captures packets on the selected network interface.
✅ **Protocol Identification**: Detects and categorizes packets based on protocol type.
✅ **Readable Output**: Displays extracted packet details in a structured format.
✅ **Lightweight & Efficient**: Uses Python's **Scapy** library for efficient packet sniffing.

---

## 🛠 Requirements

📌 **Python 3.x** installed
📌 **Scapy** library (Install using `pip`)

---

## ▶️ How to Run

### 1️⃣ Clone the Repository

```bash
   git clone https://github.com/aruvasaga-chithan/Packet-Sniffer
```

### 2️⃣ Navigate to the Project Directory

```bash
   cd Packet-Sniffer
```

### 3️⃣ Install Dependencies

```bash
   pip install scapy
```

### 4️⃣ Run the Script

```bash
   python packet_sniffer.py
```

> 🔹 On **Linux/macOS**, you might need to run the script with `sudo` to capture packets:

```bash
   sudo python packet_sniffer.py
```

---

## 📊 Usage

Once the script starts, it will begin capturing packets on the **default network interface** (Wi-Fi). Each captured packet will display the following details:

```
-------------------------------------------------
Packet: <Packet Summary>
Source IP: <Source IP Address>
Destination IP: <Destination IP Address>
Protocol: <Protocol Type>
Payload: <Decoded Payload Data>
-------------------------------------------------
```

---

## 🤝 Contribute

🔗 Fork the project, create issues, and submit pull requests!

---

## 📜 License

📝 This project is licensed under the **MIT License**.

