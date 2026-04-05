import socket
import keyboard

# Define the server address and port
server_address = ('localhost', 12345)

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print("Server is listening for a connection...")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

while True:
    try:
        # Listen for keyboard key-down events on the server
        event = keyboard.read_event(suppress=True)  # Use suppress=True to only capture keydown events

        if event.event_type == keyboard.KEY_DOWN:
            # Send the keydown event to the client
            client_socket.send(str(event).encode())
    except Exception as e:
        print(f"Error: {e}")
        break

# Close the server socket
server_socket.close()