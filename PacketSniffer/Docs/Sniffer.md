
## 🐍 `Sniffer` Class

The main class responsible for capturing raw network packets using a raw socket and parsing their contents. Acts as the entry point (or controller) of the packet inspection system.

---

---

### 🧱 Responsibilities

- Captures raw Ethernet frames using Linux socket interface.
    
- Decodes Ethernet header.
    
- Delegates IPv4 and ICMP parsing to corresponding packet classes.
    
- Organizes the parsed data into a structured dictionary format.
    

---

### 📦 Dependencies

- [[Ipv4Packet modul]]
    
- [[IcmpPacket]]
    
- Python built-in `socket`, `struct`


### ⚙️ Methods

#### `__init__() -> None`

Initializes the raw socket and packet parser instances.

---

#### `GetEthernetFrame(data: bytes) -> tuple`

Parses the Ethernet frame header and extracts:

- Destination MAC
    
- Source MAC
    
- Protocol
    
- Payload (rest of the packet after header)
#### `get_mac_addr(mac_addr: bytes) -> str`

Formats the raw MAC address bytes into a human-readable string:



#### `sniff() -> dict`

Captures a single network frame, parses it at the Ethernet and IPv4 level, and optionally parses the ICMP layer if applicable.

### 🔗 Future Extensions

You can extend the `Sniffer` class to:

- Add support for TCP, UDP, ARP, etc.
    
- Implement a continuous sniffing loop.
    
- Add packet filtering (e.g., by IP, port).
    
- Store results to a file or visualize in real-time.
