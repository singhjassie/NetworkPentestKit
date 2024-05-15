#! python3.9
import scapy.all as scapy
import optparse as op

def get_ip():
    """return ip adress passed to the script or asked at runtime, if not passed"""
    parser = op.OptionParser()
    parser.add_option("-r", "--iprange", dest="iprange", help="add ip addresses range you want to scan")
    args = parser.parse_args()[0]
    if not args.iprange:
        ip = input("Enter the ip range : ")
    else:
        ip = args.iprange
    return ip

def scan(ip_range):
    """scan the network and print ip and mac"""
    arp_packet = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_with_broadcast = broadcast / arp_packet
    answered, unanswered = scapy.srp(arp_with_broadcast,timeout = 1, verbose=False)

    print("Mac Address\t\t\tIP Address\n----------------------------------------------------")
    for element in answered:
        print(element[1][1].hwsrc + "\t\t",end="")
        print(element[1][1].psrc)

ip_range = get_ip()
scan(ip_range)
