#!/usr/bin/env python3
# server
import socket
import os
#from cryptography.fernet import Fernet


s = socket.socket()
port = 9999
server = ('localhost', port)
'''
while True:
    try:
        s.bind(server)
        break
    except:
        port -= 1
        print(f"port {port+1} failed. Trying port {port}")
    finally:
        if port == 9995:
            print("Maximum port scan reached. Terminating")
            exit()
    exit()
    break'''

'''
key = Fernet.generate_key()
key2 = b'abcdefghijklmnopqrstuvwxyz1234567890'
print(key)
k = Fernet(key)
'''

def form(x):
    x = str(x)
    x = str(x[2:len(x) - 1:]).strip()
    return x

'''
def ecrypt(x, y):
    if (y == True):
        print("Now encrypting")
        token = k.encrypt(x)
        return token
    else:
        return x


def dcrypt(x, y):
    print("Now decrypting")
    if (y == True):
        token = k.decrypt(x)
        return token
    else:
        return x
'''

def terminate():
    print("Session Terminated")
    connection.close()
    exit()


def new():
    # print("now in new")
    global creds

    print(f"Client is making an account")
    creds = [0, 0]

    username = b'Enter username'
    connection.sendall(username)
    creds[0] = form(connection.recv(100))

    password = b'Enter password'
    connection.sendall(password)
    creds[1] = form(connection.recv(100))

    # connection.sendall(b'Credentials saved. Thanks for connecting')
    appending(creds[0], creds[1])



def appending(x, y):
    print("now in appending")
    #x = form(x)
    #y = form(y)

    print(f"Username is {x} and password is {y}")
    f = open("output.txt", 'a+')
    f.write(x)
    f.write(" ")
    f.write(y)
    f.write("\n")
    f.close()
    old()


def old():
    print("Client is signing in")
    user = b'Enter Username '
    connection.sendall(user)
    username = form(connection.recv(100))

    passwd = b'Enter Password '
    connection.sendall(passwd)
    password = form(connection.recv(100))
    auth(str(username), str(password))


def auth(x, y):
    # print("Now in auth")

    print(f"Authenticating user {x} {y}")
    with open("output.txt", "r") as f:
        for line in f:
            userinfo = line.strip().split(" ")
            print(f"userinfo is {userinfo}")
            if x.lower() == userinfo[0].lower() and y == userinfo[1].lower():
                print("User Authentication is a Success")
                message = b'success'
                connection.sendall(message)
                dest(x, y)
            else:
                userinfo = line.strip().split(" ")
                print(f"User {userinfo} is not equal to {x} {y}")
        message = b'Failure'
        connection.sendall(message)
        terminate()


def dest(x, y):
    print("Now in dest")
    while True:
        try:
            message = b'would you like to chat(chat), go to docs(docs), or read your docs(read/read docs)'
            connection.sendall(message)
            received = form(connection.recv(100))
            print(f"received {received} from client")

            if str(received).lower() == 'chat':
                print("going to chat")
                chat(x, y)
            elif str(received).lower() == 'docs' or str(received).lower() == 'doc':
                print("Going to check")
                check(x, y)
            elif str(received).lower() == 'read' or str(received).lower == 'read docs':
                print("Reading docs")
                read_docs(x, y)
            elif str(received).lower() == 'encryption' or str(received).lower() == 'encrypt':
                print('not done yet. ')
                dest(x, y)
            elif str(received).lower() == 'exit':
                print("USer is leaving the server")
                terminate()
            else:
                print("chat or docs was received in error")
        except ConnectionAbortedError:
            print("Session terminated by user")
            terminate()


def check(x, y):
    # print("Now in check")
    message = b'do you have a document'
    connection.sendall(message)

    received = form(connection.recv(100))
    print(f"File exist: {received}")
    if received.lower() == 'yes' or received.lower() == 'y':
        response = b'Finding file'
        connection.send(response)
        docs(x, y)
    else:
        message = b'Creating Doc'
        connection.sendall(message)
        create_docs(x, y)


def create_docs(x, y):
    try:

        print(f"Creating file {x}.txt")

        print(f"file {x}.txt created")
        os.system(f"touch {x}.txt")
        with open(f"{x}.txt", 'w+') as f:
            f.write(f"For user {x}")
            f.write("\n")
            print(f"newline has been printed for user {x}")
            f.close()
            docs(x, y)

    except:
        print("Error making file")
        terminate()

    finally:
        # message = b'File Successfully Created'
        # connection.sendall(message)
        docs(x, y)


def docs(x, y):
    print(f"opening file {x}.txt")
    with open(f"{x}.txt", 'a+') as f:
        while True:
            try:
                received = form(connection.recv(100))
                print(f"Client -> {received}")
                f.write(f"{received}\n")

            except:
                print("error occurred while typing to docs")
                f.close()
                terminate()
                break
            finally:

                if str(received).lower() == 'exit':
                    print("User wrote quit. Sending to dest")
                    f.close()
                    dest(x, y)


def read_docs(x, y):
    f = open(f"{x}.txt")
    file = f.readlines()
    lines = 0
    for word in file:
        lines += 1
    connection.sendall(bytes(str(lines), encoding='utf-8'))
    print(f"There are {lines} lines")

    lines = 0
    c, count = 0, 0
    for lines in file:
        #Checks the first line
        print(f"Count is {count}")
        for words in file:
            #Line number
            c += 1

            #Reads line by line: words
            #print(f"The word is: {words} and c is {c}")
            for i in words:
                #counts number of characters in line
                count += 1
            connection.sendall(bytes(str(count), encoding='utf-8'))
            connection.sendall(bytes(str(words), encoding='utf-8'))
            print(f"{count}:{c}| {words}")
            count = 0

        dest(x, y)


def chat(x, y):
    print("You may now start talk. Type 'exit' to quit session")
    while True:

        try:
            data = form(connection.recv(100))
            if data.lower().strip() == 'exit':
                print("User wrote quit. Terminating")
                dest(x, y)
            print(f"Client -> {data} ")


        except:
            print("connection ended with: ", address)
            disconnect = b'Server has terminated Connection'
            connection.sendall(disconnect)
            terminate()
            exit()
            break

        finally:
            message = input('Server -> ')
            connection.sendall(message.encode())

            if str(message).lower().strip() == 'exit':
                print("Server wrote quit. terminating.")
                gen()


def gen():
    while True:

        connection.sendall(key)

        secure = True

        # send
        welcome = b"Would you like to be encrypted(yes/no):  "
        welcome = ecrypt(welcome, secure)
        connection.sendall(welcome)

        # receive
        c = form(connection.recv(100))
        print(f"User wrote {c}")
        if (c.lower() == 'yes' or c.lower() == 'y'):
            print("User Wants encryption")
            secure = True

        elif (c.lower() == 'no' or c.lower() == 'n'):
            print("User does not want encryption")
            secure = False
        elif c.lower() == 'alpha':
            print("Skipping authentication")
            dest('jo', 'dan')
        else:
            print("Invalid input")
            terminate()

        user = b'Are you a new user(yes/no)'
        connection.sendall(user)
        received = form(connection.recv(100))
        print(f"received is {received}")

        if (received.lower() == 'yes' or received.lower() == 'y'):
            print("User is new. Sending to new")
            new()
            break

        elif (received.lower() == 'no' or received.lower() == 'n'):
            print("User is old. Sending to old")
            old()
            break

        else:
            print("Invalid input")
            terminate()


print('Listening for connections')
s.listen(1)

secure = False
connection, address = s.accept()
print(f"connection established with {address}")
gen()


