import socket
import pyautogui

# Server configuration
HOST = '127.0.0.1'  # Replace with the server's IP or hostname
PORT = 12345

# Create a socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

try:
    while True:
        data = client_socket.recv(1024).decode('utf-8')

        # Parse the received data
        parts = data.split()
        action = parts[0]

        if action == 'move':
            # Extract mouse cursor coordinates from the message
            x, y = map(int, parts[1:])
            pyautogui.moveTo(x, y)
        elif action == 'click':
            # Extract click data and simulate the click
            x, y, button = map(int, parts[1:])
            pyautogui.click(x, y, button=button)

except KeyboardInterrupt:
    pass

print("Client disconnecting.")
client_socket.close()