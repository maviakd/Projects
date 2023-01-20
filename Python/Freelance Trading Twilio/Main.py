#!/usr/bin/env python3

import os

try:
    os.system("bash.exe""")
except:
    print("Please Enable the linux terminal on your machine")
    print("Simply google 'Bash terminal on  WIndows'")

try:
    import pyfiglet
except:
    inst = input("Pyfiglet is not installed. would you like to instal it?")
    if inst == 'yes' or inst == 'y':
        os.system("apt-get install python3-pyfiglet")
        print("Module installed. Please restart app")
    else:
        print("Program will not be able to start without installing modules")
        exit()

try:
    from twilio import *
    from twilio.rest import Client
except:
    inst = input("Twilio is not installed. Would you like to install it?")
    if inst == 'yes' or inst == 'y':
        try:
            os.system("apt-get instal python3-twilio")
        except:
            print("Twilio could not be started. Please start application on Linux or Bash Terminal")
            exit()
        print("Please run application on a Linux or Bash Terminal")
    else:
        print("Program will not be able to start without installing modules")
        exit()




username = 'one'
password = 'two'

admin_user = 'change'
admin_pass = 'change'


def quits(x):
    y = 'exit'
    z = 'quit'
    if x == y.lower():
        while True:
            choice = input("Would you like to Terminate or Restart ")
            if choice.lower() == 'terminate':
                print("Terminating Session")
                exit()
            elif choice.lower() == 'restart':
                print("Restarting Session")
                dest()
            else:
                print("Invalid Response")
    elif x == z.lower():
        while True:
            choice = input("Would you like to Terminate or Restart ")
            if choice.lower() == 'terminate':
                print("Terminating Session")
                exit()
            elif choice.lower() == 'restart':
                print("Restarting Session")
                dest()
            else:
                print("Invalid Response")
    else:
        return


def admin():
    Auth.new()
    auth()


def dest():

    while True:
        os.system("clear")

        print("Where would You like to go")
        choice = input("Available choices \n"
                       "Authentication \n"
                       "Clear Body/Message \n"
                       "Clear Contacts \n"
                       "Exit \n"
                       "Message \n"
                       "Credentials/Numbers \n"
                       "Body \n"
                       "Check Contacts/Contacts \n"
                       "Read Body      ")

        if choice.lower() == 'message' or choice.lower() == 'messages' or choice.lower() == 'text'\
                or choice.lower() == 'txt' or choice.lower() == 'send':
            quits(choice)
            text()
            break
        elif choice.lower() == "check contact" or choice.lower() == "check contacts":
            quits(choice)
            read_contacts()
        elif choice.lower() == 'clear contacts' or choice.lower() == 'clear contacts':
            quits(choice)
            clear_contacts()
        elif choice.lower() == 'clear' or choice.lower() == 'new' or choice.lower() == 'clear body':
            quits(choice)
            clear_body()
            break
        elif choice.lower() == 'body':
            quits(choice)
            body()
            break
        elif choice.lower() == 'auth' or choice.lower() == 'authentication':
            quits(choice)
            auth()
            break
        elif choice.lower() == 'creds' or choice.lower() == 'credential' or choice.lower() == 'credentials'\
                or choice.lower() == 'number' or choice.lower() == 'numbers':
            quits(choice)
            credential()
            break
        elif choice.lower() == 'read' or choice.lower() == 'read body':
            quits(choice)
            read_body()
        else:
            quits(choice)
            banner = pyfiglet.figlet_format("... Invalid Input...")
            print(banner)


def clear_body():
    f = open('Body.txt', 'w+')
    f.write("")
    f.close()
    banner = pyfiglet.figlet_format("...CLEARED...")
    print(banner)
    input("Press ENTER to continue...")
    dest()


def clear_contacts():
    f = open('Contacts.txt', 'w+')
    f.write("")
    f.close()
    banner = pyfiglet.figlet_format("...CLEARED...")
    print(banner)
    input("Press ENTER to continue...")
    dest()


def auth():
    while True:
        client_user = input("Username:     ")
        quits(client_user)
        client_pass = input("Password:     ")
        quits(client_pass)

        if client_user == admin_user and client_pass == admin_pass:
            print("Entering Admin Mode")
            admin()
            break
        elif username == client_user.lower() and password == client_pass:
            print("Authentication Successful")
            dest()
            break
        else:
            print("Authentication Failed")


def credential():
    while True:
        os.system("clear")
        banner = pyfiglet.figlet_format("...##########...")
        print(banner)
        try:
            x = int(input("Enter a Number:     "))
            if x == 'exit' or x == 'back' or x == 'leave' or x == "":
                print("Going Back")
                dest()

            valid = check(x)
            if valid == 10 or valid == 11:
                register(x)
                break
            else:
                print("A Valid phone number may only have 10 or 11 digits")

        except ValueError:
            print("Non Numerical character detected")


def check(x):
    numbers = 0
    for character in str(x):
        numbers += 1
    print(numbers)

    return numbers


def register(x):
    x = str(x)
    f = open("Contacts.txt", 'a+')
    f.write(x)
    f.write('\n')
    f.close()
    banner = pyfiglet.figlet_format(".....SUCCESS.....")
    print(banner)
    success = input("Number registered. pres ENTER to continue...      ")
    quits(success)
    dest()


def text():
    Twilio()
    dest()


def body():
    os.system("clear")
    banner = pyfiglet.figlet_format("...--->><<---...")
    print(banner)
    f = open("Body.txt", 'w+')
    while True:
        try:
            text = input("-->   ")
            if text == 'exit':
                banner = pyfiglet.figlet_format("...SAVED...")
                print(banner)
                input("Pres ENTER to continue...")
                f.close()
                dest()
                break
            elif text == '':
                input("Press Enter to Continue...")
                f.close()
                dest()
                break
            f.write(text)
            f.write('\n')
        except:
            #print("error occurred while typing to docs")
            f.close()
            dest()
            break

def read_contacts():
    os.system("clear")
    banner = pyfiglet.figlet_format("...CONTACTS...")
    print(banner)
    f = open("contacts.txt", 'r+')
    print("\n-\t-\t-\t-\t-\t-\t-\n")
    print(f.read())
    print("\n-\t-\t-\t-\t-\t-\t-\n")
    f.close()
    input("Press ENTER to continue...")
    dest()


def read_body():
    os.system("clear")
    banner = pyfiglet.figlet_format("...BODY...")
    print(banner)
    f = open("Body.txt", 'r+')
    print("\n-\t-\t-\t-\t-\t-\t-\n")
    print(f.read())
    print("\n-\t-\t-\t-\t-\t-\t-\n")
    f.close()
    input("Press ENTER to continue...")
    dest()


class Twilio:
    os.system("clear")

    def __init__(self):
        try:
            self.SID = input("Enter SID ->       ")
            quits(self.SID)
            self.TOKEN = input("Enter Token ->   ")
            quits(self.TOKEN)
            self.SOURCE = input("Enter Twilio Number ->      ")
            quits(self.SOURCE)
            Twilio.all_contacts(self)
        except ValueError:
            print("AUTHENTICATION FAILED. TWILIO CREDENTIALS ARE INVALID")
            dest()



    def all_contacts(self):
        b = open("Body.txt", 'r+')
        message = b.read()
        b.close()

        f = open("Contacts.txt", 'r+')
        line, word, x, y, number = 0, 0, 0, 0, 0
        lines = f.readlines()
        for x in lines:
            Twilio.send(self, x, message)
        banner = pyfiglet.figlet_format("...DONE...")
        print(banner)
        input("Press ENTER to continue...")
        dest()


    def send(self, number, message):
        print(message)
        client = Client(self.SID, self.TOKEN)
        msg = client.messages \
            .create(
            body=message,
            from_= self.SOURCE,
            to=number)
        #print(f"Message sent to {number}")


    def leave(self):
        if x == 'back' or x == 'leave' or x == 'return':
            dest()
        else:
            return


print("If errors appear above, please start run the application on a bash terminal")
print("Contact DJO for help")
banner = pyfiglet.figlet_format("... DJOS STUDIOS...")
print(banner)
auth()



