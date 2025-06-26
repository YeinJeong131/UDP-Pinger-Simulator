import random
from socket import *
serverName = 'localhost'
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, 12000))
print ('The server is running on ' + serverName)
 
while True:
    rand = random.randint(0, 10)
    message, address = serverSocket.recvfrom(1024)
    message = message.upper()
    
    if rand < 4:
        continue

    serverSocket.sendto(message, address)
