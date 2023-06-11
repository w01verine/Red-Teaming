# Created By: w01verine 2022

# The following will create a dictionary of the top used 45 ports and their OSI Model Layer


port_to_layer = {
    20: 5,    # FTP data
    21: 5,    # FTP control
    22: 4,    # SSH
    23: 4,    # Telnet
    25: 7,    # SMTP
    53: 3,    # DNS
    67: 2,    # DHCP server
    68: 2,    # DHCP client
    69: 5,    # TFTP
    80: 7,    # HTTP
    88: 5,    # Kerberos
    110: 7,   # POP3
    123: 7,   # NTP
    135: 5,   # RPC
    137: 5,   # NetBIOS name
    138: 5,   # NetBIOS datagram
    139: 5,   # NetBIOS session
    143: 7,   # IMAP4
    161: 4,   # SNMP
    162: 4,   # SNMP trap
    179: 4,   # BGP
    389: 5,   # LDAP
    443: 7,   # HTTPS
    445: 5,   # SMB
    465: 7,   # SMTPS
    514: 4,   # Syslog
    587: 7,   # SMTP (submission)
    636: 5,   # LDAPS
    993: 7,   # IMAPS
    995: 7,   # POP3S
    1080: 5,  # SOCKS
    1433: 5,  # MSSQL
    1434: 5,  # MSSQL browser
    1521: 5,  # Oracle
    1723: 3,  # PPTP
    3306: 5,  # MySQL
    3389: 3,  # RDP
    5060: 5,  # SIP
    5061: 5,  # SIP TLS
    5432: 5,  # PostgreSQL
    5631: 5,  # PCAnywhere
    5900: 5,  # VNC
    5985: 5,  # WinRM
    5986: 5,  # WinRM (SSL)
    8080: 7,  # HTTP proxy
}

'''
Layer 2 (Data Link):    DHCP server, DHCP client
Layer 3 (Network):      DNS, PPTP, RDP
Layer 4 (Transport):    SSH, Telnet, SNMP, SNMP trap, BGP, Syslog
Layer 5 (Session):      FTP data, FTP control, TFTP, Kerberos, RPC, NetBIOS name, NetBIOS datagram, NetBIOS session, LDAP, SMB, LDAPS, SOCKS, MSSQL, MSSQL browser, 
                        Oracle, MySQL, SIP, SIP TLS, PostgreSQL, PCAnywhere, VNC, WinRM, WinRM (SSL)
Layer 6 (Presentation): -
Layer 7 (Application):  SMTP, HTTP, POP3, NTP, IMAP4, HTTPS, SMTPS, SMTP (submission), IMAPS, POP3S, HTTP proxy
'''
