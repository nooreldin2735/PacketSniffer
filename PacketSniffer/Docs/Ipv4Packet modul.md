## 📦 `Ipv4Packet` Class

A subclass of `Packet` that parses and extracts relevant fields from an IPv4 packet header.

### 🧱 Inherits From

- [[Packet Modul]]
    

---

### 🎯 Purpose

`Ipv4Packet` is responsible for extracting IPv4-specific information such as:

- IP version
    
- Header length
    
- TTL (Time To Live)
    
- Protocol type
    
- Source IP address
    
- Destination IP address
### ⚙️ Methods

#### `__init__() -> None`

Initializes the IPv4-specific fields, then calls the parent constructor.


#### `get_ipv4_addr()`

Parses the IPv4 header and extracts version, header length, TTL, protocol, source IP, and destination IP.

**Returns:**  

A tuple containing:

	(version, header_length, ttl, proto, srcIp, targetIp, payload)


#### `ipv4(addr: bytes) -> str`

Converts a 4-byte IP address into standard dot-decimal notation.



