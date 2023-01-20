#Server
#!/usr/bin/env python3
import socket

s = socket.socket()
port = 9999
server = ("localhost", port)
#print("Using {} on port {}".format(*server))

busy = True
try:
        s.bind(server)
except:
        print(f"The port {port} is in use")
        port = port-1

s.listen(5)
print(f"Waiting for connection on port {port}...")

connection, address = s.accept()
while True:


        try:
                data = connection.recv(100)
                print(f"Client -> {data} ")

        except:
                print("connection ended with: ", address)
                disconnect = b'Server has terminated Connection'
                connection.sendall(disconnect)
                connection.close()
                exit()
                break

        finally:
                message = input('Server -> ')
                connection.sendall(message.encode())

