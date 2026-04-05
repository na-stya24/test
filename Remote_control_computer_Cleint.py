import socket
import pyautogui
import io
# build bytes in the right order
import struct

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cleint_socket:
    cleint_socket.connect(("127.0.0.1", 80))

    buffer = io.BytesIO()

    screenshot = pyautogui.screenshot()
    screenshot.save(buffer,format="jpeg")

    frame_data = buffer.getValue()
    frame_size= len(frame_data)
    cleint_socket.sendall(struct.pack(">L",frame_size))
    cleint_socket.sendall(frame_data)



