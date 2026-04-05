import socket
from PIL import ImageGrab
from io import BytesIO

if __name__ == "__main__":

    # create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    server_address = ('192.168.14.14', 10000)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    while True:    
        # # Take a screenshot
        screenshot = ImageGrab.grab()

        # Save the screenshot to a bytes array
        screenshot_bytes = BytesIO()
        screenshot.save(screenshot_bytes, format="PNG")
        screenshot_bytes = screenshot_bytes.getvalue() 
        # send the size of the screenshot
        size = len(screenshot_bytes)
        sock.sendall(size.to_bytes(4, byteorder='big'))

        # send the screenshot
        sock.sendall(screenshot_bytes)

    # close the socket
    sock.close()