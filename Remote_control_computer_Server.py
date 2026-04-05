import socket
import io
import struct
from PIL import Image
import cv2


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind("127.0.0.1", 80)
    server_socket.listen(1)

    cleint_socket, clent_address =server_socket.accept()

    with cleint_socket:
        print(clent_address)
        data =b""
        while len(data) < 4:
            data += cleint_socket.recv(4)
        frame_size = struct.unpack(">L", data)[0]

        data=b""
        while len(data) < frame_size:
            data += cleint_socket.recv(frame_size)
        
        frame_data = io.BytesIO(data)
        frame = Image.open(frame_data)
        frame.show()

