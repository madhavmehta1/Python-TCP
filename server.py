import socket

# Create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get server IP
host = socket.gethostname()

# Port to listen on
port = 1000

# Bind the socket to the address
server_socket.bind((host, port))

# Listen to up to 4 connections
server_socket.listen(4)

while True:
    # Start the connection
    client_socket, address = server_socket.accept()

    # Print confirmation message of connection from an address
    print("Received connection from %s " % str(address))

    # Send encoded confirmation message to client
    message = "Connected to the server \r\n"
    client_socket.send(message.encode('ASCII'))

    # Close the socket
    client_socket.close()
