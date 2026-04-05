import socket
import pyautogui
from pynput.mouse import Listener, Controller

# Server configuration
HOST = '127.0.0.1'  # Replace with the server's IP or hostname
PORT = 12345

# Create a socket and bind it to the host and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server is listening on {HOST}:{PORT}")

# Accept client connection
client_socket, client_address = server_socket.accept()
print(f"Client {client_address} connected")

# Initialize the mouse controller for simulating clicks
mouse = Controller()

# Initialize variables to store the last mouse position
last_x, last_y = pyautogui.position()

def on_move(x, y):
    global last_x, last_y
    if x != last_x or y != last_y:
        last_x, last_y = x, y
        message = f"move {x} {y}"
        client_socket.send(message.encode('utf-8'))

def on_click(x, y, button, pressed):
    if pressed:
        message = f"click {x} {y} {button}"
        client_socket.send(message.encode('utf-8'))
        # Simulate the click on the server
        mouse.position = (x, y)
        mouse.click(button)

# Start monitoring mouse move and click events
with Listener(on_move=on_move, on_click=on_click) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        pass

print("Server shutting down.")
server_socket.close()