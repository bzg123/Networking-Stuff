import struct
import socket

def create_tcp_packet(src_ip, dst_ip, src_port, dst_port, sequence=1000, ack=0, flags=0x02):
    """
    Simulate the creation of a TCP packet.
    
    Args:
        src_ip: Source IP address
        dst_ip: Destination IP address
        src_port: Source port
        dst_port: Destination port
        sequence: TCP sequence number
        ack: TCP acknowledgment number
        flags: TCP flags (0x02 = SYN, 0x01 = FIN, 0x10 = ACK)
    
    Returns:
        bytes: Complete TCP packet with IP header
    """
    
    # IP Header (simplified)
    version_header_length = (4 << 4) + 5  # IPv4, header length 5 (20 bytes)
    dscp_ecn = 0
    total_length = 20 + 20  # IP header + TCP header
    identification = 54321
    flags_fragment = 0x4000  # Don't Fragment
    ttl = 64
    protocol = 6  # TCP
    src_ip_bytes = socket.inet_aton(src_ip)
    dst_ip_bytes = socket.inet_aton(dst_ip)
    
    ip_header = struct.pack('!BBHHHBBH4s4s',
        version_header_length, dscp_ecn, total_length,
        identification, flags_fragment, ttl, protocol, 0,
        src_ip_bytes, dst_ip_bytes)
    
    # TCP Header
    data_offset_reserved = (5 << 4)  # Header length 5 (20 bytes)
    window_size = 65535

    tcp_header = struct.pack('!HHIIHHHH',
        src_port, dst_port, sequence, ack,
        data_offset_reserved << 8 | flags, window_size, 0, 0)

    packet = ip_header + tcp_header
    return packet


# Example usage
if __name__ == "__main__":
    src_ip = "192.168.1.100"
    dst_ip = "192.168.1.1"
    src_port = 5000
    dst_port = 80
    
    packet = create_tcp_packet(src_ip, dst_ip, src_port, dst_port)
    print(f"TCP Packet created: {packet.hex()}")
    print(f"Packet size: {len(packet)} bytes")