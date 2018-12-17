#!/usr/bin/env
import socket

# Create a client socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get server ip information
target_host = socket.gethostname()
target_port = 9999

# Connect the client to the address
client_socket.connect((target_host, target_port))

# Send encoded data
message = "ABCDEF"
client_socket.send(message.encode("ASCII"))

# Receieve response data
response = client_socket.recv(1024)

# Print decoded message
print "Decoded message:" + response.decode("ASCII")