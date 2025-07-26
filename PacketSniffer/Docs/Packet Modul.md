## 🧱 `Packet` Class (Base Packet)

A base class for representing raw network packets. This class is designed to be extended by specific packet types like `IPv4Packet`, `IcmpPacket`, and more in the future.

### 📦 Purpose

`Packet` provides the foundational structure for all packet types. It holds raw packet data and basic Ethernet-level metadata such as source/destination MAC addresses and Ethernet protocol type.

### ⚙️ Methods

#### `__init__() -> None`

Initializes an empty `Packet` object with default values.

#### `init_data(data)`

Stores raw binary packet data for further parsing by subclasses.


### 🔗 Usage

This class is not intended to be used directly. Instead, it should be subclassed:


### Future Expansion

You can extend this class to support:

- `UdpPacket`
    
- `TcpPacket`
    
- `ArpPacket`
    
- `DnsPacket`, etc.
    

Each subclass will implement protocol-specific parsing logic using the `data` attribute initialized via `init_data()`.