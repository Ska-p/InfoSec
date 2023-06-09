# Project for the Information Security course, A.Y. 2022/23

The detailed documentation is provided in .pdf version, inside the [doc](https://github.com/Ska-p/InfoSec/tree/main/doc) folder.

![Slide1](https://github.com/Ska-p/InfoSec/assets/102731992/8eed5ff8-af7b-41ef-bb1a-bb8affcb01e8)

## Network Implementation Summary

LAN: The local area network (LAN) uses the IP range 192.168.170.0/24 and consists of 5 routers connected via the Routing Information Protocol (RIP). A Kali Client machine is also included.

CLIENTS: This network includes a Kali machine (internal attacker).

SERVERS: The SIEM Splunk service is hosted in this network, accessed by the Kali Internal machine (attacker and defender). Also, a Windows XP machine (used as victim) is included.

DMZ1: The DMZ1 network houses a web server accessible from both internal and external networks. The IP range for this network is 192.168.173.0/24.

Scalability: The LAN network is assigned the IP range 192.168.170.0/24, while the other networks use subsequent IP ranges: 192.168.171.0/24, 192.168.172.0/24, and 192.168.173.0/24 for CLIENTS, DMZ1, and SERVERS respectively.

## Attacks implementation

+ 2 Reconnaissance Attacks
+ 3 Denaial of Service Attacks
+ 1 Extra Attack: RIP poisoning

The script for the attacks are written by using python with [Scapy libraries](https://scapy.readthedocs.io/en/latest/introduction.html). Those script are very simple and easy to understand so there is no comment in the code.

## Defense implementation

For defensive strategies, we opted for SIEM Splunk as our Intrusion Detection System (IDS). Additionally, in order to also prevent the attacks, we implemented the Palo Alto Advanced Defense mechanism, which facilitates efficient traffic analysis and works as IDS and Intrusion Prevention System (IPS) as well. Policies and Zone protection profiles were defined by following [Palo Alto documentation](https://docs.paloaltonetworks.com/content/dam/techdocs/en_US/pdf/pan-os/9-1/pan-os-web-interface-help/pan-os-web-interface-help.pdf) and Splunk rules were implemented with [Splunk Search Processing Language (SPL)](https://docs.splunk.com/Documentation/Splunk/latest/SearchTutorial/Usethesearchlanguage)
