import netfilterqueue as netq
import scapy.all as scapy

def work_packet(packet):
    use_packet = scapy.IP(packet.get_payload())
    print(use_packet.show())
    #Play with the packet here


queue = netq.Netfilterqueue()
queue.bind(0, work_packet)
queue.run()