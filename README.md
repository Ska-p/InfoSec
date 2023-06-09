## Project for the Information Security course, A.Y. 2022/23

The detailed documentation is provided in .pdf version, inside the doc folder.

![Network_structure_updated_2.pdf](https://github.com/Ska-p/InfoSec/files/11710111/Network_structure_updated_2.pdf)

Network Implementation Summary:

LAN: The local area network (LAN) uses the IP range 192.168.170.0/24 and consists of 5 routers connected via the Routing Information Protocol (RIP). A Kali Client machine is also included.

CLIENTS: This network includes a Kali machine (internal attacker).

SERVERS: The SIEM Splunk service is hosted in this network, accessed by the Kali Internal machine (attacker and defender). Also, a Windows XP machine (used as victim) is included.

DMZ1: The DMZ1 network houses a web server accessible from both internal and external networks. The IP range for this network is 192.168.173.0/24.

Scalability: The LAN network is assigned the IP range 192.168.170.0/24, while the other networks use subsequent IP ranges: 192.168.171.0/24, 192.168.172.0/24, and 192.168.173.0/24 for SERVERS, CLIENTS, and DMZ1 respectively.
