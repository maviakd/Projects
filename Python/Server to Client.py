import socket
goodbey = b'Thank you. Terminating session. Goodbey'

s = socket.socket()
port = 9999
server = ('localhost', port)
s.bind(server)


def new():
        global creds
        print(f"Client is making an account")
        creds = [0, 0]

        username = b'Enter username'
        connection.sendall(username)
        creds[0] = connection.recv(100)

        password = b'Enter password'
        connection.sendall(password)
        creds[1] = connection.recv(100)

        connection.sendall(b'Credentials saved. Thanks for connecting')
        appending(str(creds[0]), str(creds[1]))
        connection.close()
        exit()

def old():
        print("Client is signing in")
        user = b'Enter Username '
        connection.sendall(user)
        username = connection.recv(100)

        passwd = b'Enter Password '
        connection.sendall(passwd)
        password = connection.recv(100)
        auth(str(username), str(password))


def appending(x, y):
    x = x[2:len(x) - 1:]
    y = y[2:len(y) - 1:]
    print(f"Username is {x} and password is {y}")
    f = open("output.txt", 'a+')
    f.write(x)
    f.write(" ")
    f.write(y)
    f.write("\n")
    chat()
    connection.close()
    exit()


def auth(x, y):
    x = x[2:len(x) - 1:]
    y = y[2:len(y) - 1:]
    account = str(x + " " + y)

    f = open("output.txt", 'r')
    print(f"Authenticating User {account}")
    x = f.read()

    for i in x:
        check = bool(i == account)
        if check == True:
            message = b'Success, So here we go'
            print(message)
            connection.sendall(message)
            f.close()
            chat()
            break
        else:
            message = b'Failure, but im taking you anyways'
            print(message)
            connection.sendall(message)
            f.close()
            chat()
            break
    x = f.read()
    f.close()
    connection.close()

def chat():
    print("You may now start talk")
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


print('Listening for connections')
s.listen(1)

waiting = True
while waiting:
        global connection
        connection, address = s.accept()
        print(f"connection established with {address}")

        banner = b"Welcome to Djos Studios. Are you a new user?(Yes/No):  "
        connection.sendall(banner)

        received = connection.recv(100)
        print(f"received is {received}")
        while True:
            try:
                if (received.lower() == b'yes' or received.lower() == b'y'):
                    print("User is new. Sending to new")
                    new()
                    break

                elif (received.lower() == b'no' or received.lower() == b'n'):
                    print("User is old. Sending to old")
                    old()
                    break

                else:
                    print("Invalid input")
                    connection.sendall(goodbey)
                    connection.close()
                    break
            except ValueError:
                print("only numbers")




