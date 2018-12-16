import socket

# Create socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get server ip
host = socket.gethostname()

# Port to listen on
port = 1000

# Connect the socket to the address
client_socket.connect((host, port))

# Message that recieves a maximum of 1024 bytes
message = client_socket.recv(1024)

# Close the socket
client_socket.close()

# Print the decoded message
print(message.decode('ASCII'))