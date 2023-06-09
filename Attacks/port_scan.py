from scapy.all import *
from scapy.layers.inet import TCP, IP
import socket

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

startport = int(sys.argv[1])
endport = int(sys.argv[2])

if startport == endport:
    endport += 1

file = open("sweep_results.txt")
lines = file.readlines()


for line in lines[1:]:
    line = line.rstrip()
    print("Scanning " + line + " for open TCP ports in range (" + str(startport) + " - " + str(endport) + ").")
    for port in range(startport, endport):
        packet = IP(dst=line) / TCP(dport=port, flags="S")
        response = sr1(packet, timeout=0.01, verbose=0)
        if response and response.getlayer(TCP).flags == 0x12:
            service = socket.getservbyport(port)
            print("Port " + str(port) + " " + service + " is open")
            sr1(IP(dst=line)/TCP(dport=port, flags="R"), timeout=1, verbose=0)