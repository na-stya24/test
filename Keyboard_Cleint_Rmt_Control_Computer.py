import socket
import keyboard

# Define the server address and port
server_address = ('localhost', 12345)

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(server_address)

while True:
    try:
        # Receive keyboard events from the server
        data = client_socket.recv(1024).decode()
        
        # Simulate the event on the client
        keyboard.play(keyboard.read_event(s=data))
    except Exception as e:
        print(f"Error: {e}")
        break

# Close the client socket
client_socket.close()