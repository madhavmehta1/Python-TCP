import socket
import threading

bind_ip = socket.gethostname()
bind_port = 9999

# Create server socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server socket to the address
server_socket.bind((bind_ip, bind_port))

# Receive up to 5 connections
server_socket.listen(5)

print"[*] Listening on %s:%d" % (bind_ip,bind_port)

def handle_client(client_socket):
    # Print out what the client sends
    request = client_socket.recv(1024)

    # Print confirmation message of connection from an address
    print "[*] Decoded message received: %s" % request.decode("ASCII")

    # Send back data packet
    message = "You have successfully connected to the server"
    client_socket.send(message.encode('ASCII'))

    # Close the socket
    client_socket.close()


while True:
    # Start the connection
    client, address = server_socket.accept()

    # Print confirmation message of connection from an address
    print "[*] Accepted connection from: %s:%d" % (address[0], address[1])

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()