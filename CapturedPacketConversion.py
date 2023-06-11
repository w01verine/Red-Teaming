# Written By: Tommie Navitskas 2022

# This code extracts basic information from captured packets and sorts them based on certain criteria.


import sqlite3
import struct

# create a SQLite database to store the packet information
conn = sqlite3.connect('packet_info.db')
c = conn.cursor()

# create a table to store the packet information
c.execute('''CREATE TABLE packets
             (id INTEGER PRIMARY KEY,
              timestamp INTEGER,
              src_mac TEXT,
              dst_mac TEXT,
              eth_type INTEGER,
              ip_src TEXT,
              ip_dst TEXT,
              ip_proto INTEGER,
              tcp_src INTEGER,
              tcp_dst INTEGER,
              udp_src INTEGER,
              udp_dst INTEGER,
              bgp AS (ip_proto == 6 AND (tcp_dst == 179 OR tcp_src == 179)))''')

# function to parse Ethernet header
def parse_ethernet_header(data):
    eth_header = struct.unpack('!6s6sH', data[:14])
    src_mac = ':'.join('%02x' % b for b in eth_header[0])
    dst_mac = ':'.join('%02x' % b for b in eth_header[1])
    eth_type = eth_header[2]
    return src_mac, dst_mac, eth_type, data[14:]

# function to parse IP header
def parse_ip_header(data):
    ip_header = struct.unpack('!BBHHHBBH4s4s', data[:20])
    ip_proto = ip_header[6]
    ip_src = socket.inet_ntoa(ip_header[8])
    ip_dst = socket.inet_ntoa(ip_header[9])
    return ip_proto, ip_src, ip_dst, data[20:]

# function to parse TCP header
def parse_tcp_header(data):
    tcp_header = struct.unpack('!HHLLBBHHH', data[:20])
    tcp_src = tcp_header[0]
    tcp_dst = tcp_header[1]
    return tcp_src, tcp_dst

# function to parse UDP header
def parse_udp_header(data):
    udp_header = struct.unpack('!HHHH', data[:8])
    udp_src = udp_header[0]
    udp_dst = udp_header[1]
    return udp_src, udp_dst

# function to parse BGP header
def parse_bgp_header(data):
    bgp_header = struct.unpack('!BBH', data[:4])
    magic_bit = bgp_header[0]
    return magic_bit

# main loop to capture and analyze packets
while True:
    packet = capture_packet()  # replace this with your own code to capture a packet
    timestamp = get_current_time()  # replace this with your own code to get the current timestamp
    
    src_mac, dst_mac, eth_type, eth_data = parse_ethernet_header(packet)
    
    if eth_type == 0x0800:  # IPv4
        ip_proto, ip_src, ip_dst, ip_data = parse_ip_header(eth_data)
        
        if ip_proto == 6:  # TCP
            tcp_src, tcp_dst = parse_tcp_header(ip_data)
        elif ip_proto == 17:  # UDP
            udp_src, udp_dst = parse_udp_header(ip_data)
        
        # insert the packet information into the database
        c.execute("INSERT INTO packets VALUES (NULL, ?, ?, )
