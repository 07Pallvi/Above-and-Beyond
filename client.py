# Pallvi - 2110994824

# import the socket module
from socket import *
# define the port number and IP address of server
serverPort = 13500
serverName = "192.168.108.133"
# create the UDP client socket
clientsocket = socket(AF_INET, SOCK_DGRAM)

# client sends hello message to the server
message = "Hello"
clientsocket.sendto(message.encode(), (serverName, serverPort))
servermessage, serverAddress = clientsocket.recvfrom(2048)
print(servermessage.decode())
# asks user to enter his/her name and send it to server
message = input()
clientsocket.sendto(message.encode(), (serverName, serverPort))
# print the welcome message received from server
servermessage, serverAddress = clientsocket.recvfrom(2048)
print(servermessage.decode())

# closes the client socket
clientsocket.close()