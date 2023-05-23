import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 8000)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server is listening on {}:{}'.format(server_address[0], server_address[1]))

while True:
    # Wait for a connection
    print('Waiting for a connection...')
    client_socket, client_address = server_socket.accept()
    print('Accepted connection from {}:{}'.format(client_address[0], client_address[1]))

    try:
        # Receive data from the client
        data = client_socket.recv(1024)
        print('Received data: {}'.format(data.decode()))

        # Send a response back to the client
        response = 'Hello from the server!'
        client_socket.sendall(response.encode())
        print('Sent response: {}'.format(response))
    finally:
        # Close the connection
        client_socket.close()
