## 📦 `IcmpPacket` Class

A subclass of `Packet` that parses and extracts fields from an ICMP (Internet Control Message Protocol) packet.

### 🧱 Inherits From

- [[Packet Modul]]
    

---

### 🎯 Purpose

`IcmpPacket` is designed to handle ICMP-specific parsing from raw packet data. It extracts:

- ICMP type (e.g., 8 = Echo request, 0 = Echo reply)
    
- Code (subtype for the ICMP type)
    
- Checksum
    
- Payload (remaining bytes after the header)
    

---

### ⚙️ Methods

#### `__init__() -> None`

Calls the parent `Packet` constructor. No additional fields are initialized here, as ICMP packets are typically simple.

#### `icmp_packet() -> tuple`

Parses the first 4 bytes of an ICMP packet to extract:

- Type
    
- Code
    
- Checksum
    

Then returns the remaining payload.

