# Tello Python3 Control Demo
# http://www.ryzerobotics.com/

# Theses are the modules that are being imported while running the code.
import threading
import socket
import sys
import time
import pytest
from datetime import date
import sys
import sqlite3

host = ''
port = 9000
locaddr = (host,port)


# The software start with creating a UDP socket
# This socket allows the computer to connect to the drone.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Here are the ip-address and port of the drone that are used for the socket connection.
tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    # This function decodes the message that the drone sends to the user.
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break

@pytest.fixture()
def drone_connected():
    # This function checks if the drone network is connected to the user's PC.
    # It compares the IP address the PC is getting with the actual drone's IP address.
    hostname = socket.gethostname()
    IPaddress = socket.gethostbyname(hostname)
    if IPaddress[0:10] == '192.168.10':
        return True
    # if IPaddress == '127.0.0.1': # This IP gets returned when there is no internet connection.
        # return False
    else:
        return False

@pytest.fixture()
def help_command():
    # This function shows the instruction of all the commands for the drone.
    # This would be helpful to the user who does not know the command.
    instruction = """
    Here are the commands that you can use:
    1. For auto takeoff and land:
        - takeoff
        - land
    2. For moving drone by xx distance (xx is ranged from 20 to 500cm):
        - up xx
        - down xx
        - left xx
        - right xx
        - forward xx
        - back xx
    3. For rotating drone by x much degree (xx is from 1 to 3600degree):
        - cw xx (clockwise rotation)
        - ccw xx (counter-clockwise rotation)
    4. For flipping to x direction
       (x has many options: l (left), r (right), f (forward), b (back)
        bl (back/left), rb (back/right), fl (front/left), fr (front/right) ):
        - flip x
    5. For changing the speed by x much (x is from 1 to 100cm/s)
        - speed xx
    6. For reading the current value
       (Caution: Capital letter! Don't for question mark!):
        - speed?  : shows current speed
        - battery? : shows current battery percentage
        - time? : shows current flight time
    """
    return instruction

# These two classes below allow to have a class instance for the pilot and flight.
# The pilot instance may have more functions later on, but now the name can be saved.
# For the flight instance, there are two method functions, which are used to save the amount of battery left and total flight time.
class pilot():
    count = 0
    def __init__(self,name):
        self.name = name
        pilot.count += 1

class flight():
    date = date.today()
    def __init__(self,battery=None,flight_time=None):
        self.battery = battery
        self.flight_time = flight_time
    def battery_left(self,amount):
        self.battery = amount
        return self.battery
    def flight_total(self,amount):
        self.flight_time = amount
        return self.flight_time

# From here, the main function starts and the user actually gets to see in the command line.
def main():
    # Fisrt, the function will automatically check if the user's PC is well connected to the drone.
    if drone_connected() == False:
        print("\nSorry, it looks like you have not successfully connected to the drone yet!\nPlease try again after connecting to the drone")
        sock.close()
        sys.exit()

    # Here, PC is getting ready to send to and receive from the drone.
    #recvThread create
    recvThread = threading.Thread(target=recv)
    recvThread.start()

    # Once the connection is made successfully, the software shows these lines below. The lines will be shown in the Demo again.
    print ('\r\n\r\nWelcome!\r\n')

    name_pilot = input("What is your name, pilot? ")
    print("Hello,",name_pilot +". Let's have some fun with the drone!\n")
    # Here, the class instances are made.
    new_pilot = pilot(name_pilot)
    new_flight = flight()
    print ('\nPlease type "command" to start commanding the drone.\n')
    print ('Once the command interpreter returns "OK", type any command lines.\n')
    time.sleep(1)
    print ('\nIf need command instructions, type "help command".\n')
    print ('If you type something not in the command instruction, nothing will happen.\n')
    time.sleep(1)
    print ('\nIf want to disconnect, type "end".\n')
    time.sleep(1)

    while True:
        # Here, the user gets to choose which mode they would like to use.
        mode_select = input("Which mode do you want to use, automatic or manual?\nType either 'a' for automatic or 'm' for manual: ")

        # If the user selects manual mode, it will go down here.
        if mode_select == 'm':
            print("\nYou selected 'manual mode'! Please type 'command' to start.")
            while True:
                msg = input("")
                # The user fisrt need to type "command" to start.
                # Until "command" is typed, the while loop will be continued.
                if  msg == "command":
                    msg = msg.encode(encoding="utf-8")
                    sent = sock.sendto(msg, tello_address)
                    break
                else:
                    print("please type 'command' first\n")

            while True:

                try:
                    if drone_connected() == False:
                        print("\nSorry, it looks like you lost connection!\nPlease try again after connecting to the drone")
                        sock.close()
                        break

                    # Now the user can do the any commands such as takeoff and land.
                    msg = input("\nplease type any command lines: ")

                    # The user can learn the kinds of commands here if type help command.
                    if msg == "help command":
                        print(help_command())

                    # Once the user is done, he/she should type "end" to finish the program.
                    if 'end' in msg:
                        # new_flight.battery_left()
                        # new_flight.flight_total()
                        print ('...')
                        sock.close()
                        break

                    # Here, the command that the user typed is encoded so that the drone could understand it.
                    # Then the encoded message is sent to the drone through the socket.
                    msg = msg.encode(encoding="utf-8")
                    sent = sock.sendto(msg, tello_address)
                    time.sleep(2)

                except KeyboardInterrupt:
                    print ('\n . . .\n')
                    sock.close()
                    break

            print("I hope you enjoyed flying drone," + new_pilot.name)

            # Once the user is done playing with the drone, there are a few quesitons that will be asked to record some information.
            # The info will be saved in the form of dictionary and the variable "flight_metadata" will indicate the location to those info.
            flight_metadata = {"Pilot_Name":new_pilot.name , "Flight_Note":None, 'Temp':None, 'Location':None, 'Time':new_flight.date}

            flightnote = input('If you want to record flight note, type here. If not, press enter. ')
            temperature = input('If you want to record the temperature(°F) right now, type here. If not, press enter. ')
            location = input('If you want to record the location where you flied drone, type here. If not, press enter. ')

            flight_metadata["Flight_Note"] = flightnote
            flight_metadata["Temp"] = temperature
            flight_metadata["Location"] = location

            ### DATABASE STORAGE ###
            # We used database called SQlite3 to save the info.
            conn = sqlite3.connect("Drone_Database.db")

            cur = conn.cursor()

            res = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
            table_list = cur.fetchall()
            # Fisrt, the table will be made if there is no table.
            # There are five attributes for now, but there may be more later on.
            if len(table_list) == 0:
                cur.execute('CREATE TABLE flight_metadata (Pilot_Name, Flight_Note, Temperature, Location, Date)')
            else:
                for table in table_list:
                    if 'flight_metadata' not in table:
                        cur.execute('CREATE TABLE flight_metadata (Pilot_Name, Flight_Note, Temperature, Location, Date)')

            values = tuple(flight_metadata.values())
            # Then the info will be inserted into the table.
            cur.execute('INSERT INTO flight_metadata values(?,?,?,?,?)', values)

            conn.commit()
            break

        # Beofre, if the user selects atomatic mode, the code will directly come down here and break
        # because the mode is under development now.
        elif mode_select == 'a':
            print("\nSorry, this mode is currently under development.")
            sock.close()
            break

        # If the user types wrong command for selecting mode, it will ask the user to type again.
        else:
            print("\nWrong command! Please Type again\n")

if __name__ == "__main__":
    main()
