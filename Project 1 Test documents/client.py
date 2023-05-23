import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('localhost', 8000)
client_socket.connect(server_address)

try:
    # Send data to the server
    message = 'Hello from the client!'
    client_socket.sendall(message.encode())
    print('Sent data: {}'.format(message))

    # Receive the server's response
    response = client_socket.recv(1024)
    print('Received response: {}'.format(response.decode()))
finally:
    # Close the connection
    client_socket.close()
