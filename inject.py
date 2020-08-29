import netfilterqueue as netq
import scapy.all as scapy

def work_packet(packet):
    use_packet = scapy.IP(packet.get_payload())
    if use_packet.haslayer(scapy.Raw):
        if use_packet[scapy.TCP].dport == 80:
            print("REQUEST##############")
            print(use_packet.show())
        elif use_packet[scapy.TCP].sport == 80:
            print("RESPONSE#############")
            print(use_packet.show())

    packet.accept()


queue = netq.NetfilterQueue()
queue.bind(0, work_packet)
queue.run()