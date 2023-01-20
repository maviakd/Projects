import socket

s = socket.socket()
port = 9999
server = ('localhost', port)
s.connect(server)

session = True
inner = True

def gen():
        x = s.recv(100)
        print(x)

        message = input("Client -> ")
        s.sendall(message.encode())

        #message = message[2:len(message) - 1:]
        if (message.lower() == 'yes' or message.lower() == 'y'):
            print("Make an account")
            new()
        elif (message.lower() == 'no' or message.lower() == 'n'):
            print("Sign in")
            old()
        else:
            print(f"Invalid input. User entered {message}")
            s.close()

def new():
    while True:

        received = s.recv(100)
        print(received)
        message = input("Client -> ")
        s.sendall(message.encode())

        received2 = s.recv(100)
        print(received2)
        message2 = input("Client -> ")
        s.sendall(message2.encode())

        received3 = s.recv(100)
        print(received3)
        chat()
        break

def old():
    while True:
        received = s.recv(100)
        print(received)
        message = input("Client -> ")
        s.sendall(message.encode())

        received2 = s.recv(100)
        print(received2)
        message2 = input("Client -> ")
        s.sendall(message2.encode())

        received3 = s.recv(100)
        print(f"Log in is a {received3}")
        chat()
        break

def chat():
    print("You many now start to talk")
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

gen()

