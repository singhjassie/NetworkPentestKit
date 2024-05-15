import subprocess as sp
from optparse import OptionParser
import re
from random import choice

# function definitions
def get_arguments():
    """return arguments passed while running python script or ask at runtime"""
    parser = OptionParser()
    parser.add_option("-m", "--mac", dest = "mac_address", help = "To give the new mac address")
    parser.add_option("-i","--interface", dest = "interface", help="To give the interface name")
    values,arguments = parser.parse_args()
    if not values.mac_address:
        values.mac_address = get_random_mac()
        # parser.error("MAC address not given!")
    if not values.interface:
        values.interface = input("Enter the interface name : ")
        # parser.error("Interface not given!")
    if not check_interface_existance(values.interface):
        parser.error("Interface does not exist!")
    return values

def get_random_mac():
    """create and return a valid random mac address"""
    hex_digits = "0123456789abcdef"
    even_digits = "02468"
    mac = ""
    for i in range(6):
        if mac=="":
            mac += choice(hex_digits) + choice(even_digits)
        else:
            mac += ":" + choice(hex_digits) + choice(hex_digits)
    return mac


def check_interface_existance(interface):
    """check if passed interface exist or not"""
    ip_link_show_output= sp.getoutput("ip link show")
    searched_interfaces=re.search(interface + ":", ip_link_show_output)
    if searched_interfaces:
        return searched_interfaces.group(0)

def change_mac(new_mac,interface):
    """change mac address of interface and return none"""
    print(f"[+] Changing mac address......")
    sp.call(["ip", "link", "set", interface, "down"])
    sp.call(["ip", "link", "set",interface,"address",new_mac])
    sp.call(["ip", "link", "set",interface,"up"])

def verify_new_mac(new_mac, interface):
    """verify that macaddress actually changed or not"""
    ip_link_output=sp.getoutput(f"ip link show {interface}")
    current_mac_address=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ip_link_output)
    if current_mac_address.group(0)==new_mac:
        print(f"[+] Mac Address changed to {new_mac}")
    else:
        print("[-] MAC address is not changed!")


# main
arg_values=get_arguments()
change_mac(arg_values.mac_address, arg_values.interface)
verify_new_mac(arg_values.mac_address, arg_values.interface)