# Created By: w01verine 2022

# The following displays the attack method based on the provided protocol

def attackMethod(protocol):
    if protocol in ['HTTP', 'FTP', 'SMTP', 'DNS']:
        print('Exploit')
    elif protocol in ['RPC', 'SIP', 'RTP']:
        print('Phishing')
    elif protocol in ['SSL', 'SNMP', 'XMPP']:
        print('Hijacking')
    elif protocol in ['TCP', 'UDP', 'SCTP', 'DCCP']:
        print('Reconnaissance')
    elif protocol in ['IPv4', 'IPv6', 'ICMP', 'IGMP']:
        print('Man In The Middle')
    elif protocol in ['Ethernet II', 'IEEE 802.1Q', 'PPP', 'HDLC', 'ARP']:
        print('Spoofing')
    elif protocol in ['IEEE 802.3', 'IEEE 802.11', 'IEEE 802.15.1', 'IEEE 802.15.4']:
        print('Sniffing')
    else:
        print('Protocol not found')
