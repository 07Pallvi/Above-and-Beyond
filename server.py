# Pallvi - 2110994824

# import the socket module
from socket import *

# define server port number
serverPort = 13500
# create server socket and bind to the port
serversocket = socket(AF_INET, SOCK_DGRAM)
serversocket.bind(('', serverPort))
print("The server is listening")

while True:
    # server receives the hello message and asks for client name
    hellomessage, clientAddress = serversocket.recvfrom(2048)
    message = "Hello, What's your name?"
    serversocket.sendto(message.encode(), clientAddress)
    # receives client name and responds with welcome message
    clientmessage, clientAddress = serversocket.recvfrom(2048)
    message = "Hello " + clientmessage.decode() + ", Welcome to SIT202"
    print(message)
    serversocket.sendto(message.encode(), clientAddress)
