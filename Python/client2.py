#!/usr/bin/env python3
# client

import socket
#from cryptography.fernet import Fernet
import pyfiglet

s = socket.socket()
port = 9999
ip = '192.168.43.109'
local = 'localhost'
server = (local, port)

while True:
    try:
        s.connect(server)
        break
    except:
        port -= 1
        print(f"port {port+1} failed. Trying port {port}")
    finally:
        if port == 9995:
            print("Max port scanned reached. Terminating")
            break

#key = Fernet.generate_key()


'''
def dcrypt(x, y, key):
    if y == True:
        print("now decrypting")
        print(f"x is {x}")
        token = k.decrypt(x)
        print(token)
        try:
            token = k.decrypt(x)
            return token
        except:
            print("Error decoding Terminating")
            terminate()
    else:
        return x


def ecrypt(x, y):

    print("Now encrypting")
    if y == True:
        token = k.encrypt(x)
        print("word encrypted")
        return token
    else:
        return x
'''

def form(x):
    x = str(x)
    x = str(x[2:len(x) - 1:])
    return x


def terminate():
    print("Connection Terminated")
    s.close()
    exit()


def gen():
	#print("Now in GEN")
	while True:
		
		banner = pyfiglet.figlet_format("           #Welcome#")
		print("#######################################################################################################################")
	
		print(f"                               {banner}")
		print("#######################################################################################################################")

		x = form(s.recv(100))
		print(x)

		while True:
			message = input("Client -> ")
			if (message.lower() == 'yes' or message.lower() == 'y'):
				print("Make an account")
				s.sendall(message.encode())
				new()
			elif (message.lower() == 'no' or message.lower() == 'n'):
				s.sendall(message.encode())
				old()
			print(f"Invalid Input. Yes or No(y/n)\n{x}")


def new():
    while True:
        print("Create an account")
        received = form(s.recv(100))
        print(f"Server -> {received}")

        message = input("Client -> ")
        s.sendall(message.encode())

        received2 = form(s.recv(100))
        print(f"Server -> {received2}")

        message2 = input("Client -> ")
        s.sendall(message2.encode())

        old()
        break


def old():
    #print("Sign in")
    while True:
        received = form(s.recv(100))
        print(f"Server -> {received}")
        message = input("Client -> ")
        s.sendall(message.encode())

        received2 = form(s.recv(100))
        print(received2)
        message2 = input("Client -> ")
        s.sendall(message2.encode())
        auth()


def auth():
    #print("now in auth")
    received3 = form(s.recv(7))
    print(f"We received {received3}")

    if received3.lower().strip() == 'success':
        print(f"Log in is a {received3}")
        dest()
    elif received3.lower().strip() != 'success':
        print(f"Failed received is {received3}")
        terminate()


def dest():
    #print("now in dest")
    print("Write 'exit' to leave")
    received = form(s.recv(100))
    print(f"server -> {received}")

    while True:
        message = input("Client -> ")
        try:
            if message.lower() == 'chat':
                print("going to chat")
                s.sendall(message.encode())
                chat()
            elif message.lower() == 'docs' or message.lower() == 'doc':
                print("check for docs")
                s.sendall(message.encode())
                check()
            elif message.lower() == 'read' or message.lower() == 'read docs':
                print("going to read document")
                s.sendall(message.encode())
                read_docs()
            elif message.lower() == 'encryption' or message.lower() == 'encrypt':
                print('not done yet')
                s.sendall(message.encode())
                dest()
            elif message.lower() == 'exit':
                terminate()
            print(f"Invalid input. Enter (chat/docs/read)\n{received}")
        except ConnectionAbortedError:
            print("Session terminated by server")
            terminate()

def check():
    #print("welcome to check")
    received = form(s.recv(100))
    print(f"Server -> {received}")

    while True:
        message = input("client -> ")
        if message.lower() == 'yes' or message.lower() == 'no':
            s.sendall(message.encode())
            break
        else:
            print(f"Invalid input\n{received} ")

    if message.lower() == 'yes':
        chk = form(s.recv(100))
        print(f"server -> {chk}")
        docs()
    elif message.lower() == 'no':
        chk = form(s.recv(100))
        print(f"server ->{chk}")
        docs()
    else:
        print("Error getting result in check sequence")
        terminate()


def docs():
    print("Begin Typing. Write 'exit' to exit")
    while True:
        try:
            x = input("client-> ")
            s.sendall(x.encode())
        except:
            print("Error occured while typing in docs")
            terminate()
        finally:
            if x.lower() == 'exit':
                print("Closing docs")
                dest()

def doc_form(x):
    x = str(x)
    x = str(x[:len(x)-2])
    return x

def read_docs():

    lines = form(s.recv(2))
    print(f"There are is a total of {lines} lines")

    while True:
        for x in range(int(lines)):
            words = form(s.recv(2))
            try:
                line = form(s.recv(int(words)))
                print(doc_form(line))
            except:
                linex = line[:len(line)-1]
                print(doc_form(linex))
        break
    dest()

    dest()



def chat():
    print("You many now start to talk")
    while True:
        try:
            message = input('Client -> ')
            s.sendall(message.encode())
            if message.lower().strip() == 'exit':
                print("Session terminated by Client")
                dest()
        except:
            print("Terminating session")
            terminate()
            break
        finally:
            received = form(s.recv(100))
            print(f"Server -> {received}")

            if received.lower().strip() == 'exit':
                print("Session terminated by Server")
                dest()


gen()

