#Client

#!/usr/bin/env python3
import socket

s = socket.socket()
port = 8080
server = ('localhost', port)


try:
        s.connect(server)
except:
        print(f"No server found on port {port}\nUsing port {port-1}")
        port = port-1

print("Connection established")

while True:
        try:
                message = input('Client -> ')
                s.sendall(message.encode())

                received = s.recv(100)
                print(f"Server -> {received}")
        except:
                print("Terminating session")
                s.close()
                break







