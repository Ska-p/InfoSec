from scapy.all import *
import ipaddress
import logging
import sys

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

network = str(sys.argv[1])
print("Sweeping " + network + " for possible victims")

ip_addresses = list(ipaddress.IPv4Network(network).hosts())

reachable_hosts = []

for ip in ip_addresses:
    packet = IP(dst=str(ip))/ICMP()
    response = sr1(packet, timeout=0.1, verbose=0)
    if response is not None:
        if response.haslayer(ICMP) and response[ICMP].type != 11:
            print("Host reachable: " + str(ip))
            reachable_hosts.append(str(ip))

with open("sweep_results.txt", 'w') as file:
    for ip in reachable_hosts:
        file.write(ip + "\n")

print("Scan completed. Found " + str(len(reachable_hosts)) + " reachable hosts.")