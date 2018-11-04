# Tello Python3 Control Demo
# http://www.ryzerobotics.com/

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


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break

def drone_connected():
    hostname = socket.gethostname()
    IPaddress = socket.gethostbyname(hostname)
    if IPaddress == '127.0.0.1': # This IP gets returned when there is no internet connection.
        return False
    else:
        return True

@pytest.fixture()
def help_command():
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

def main():
    if drone_connected() == False:
        print("\nSorry, it looks like you have not successfully connected to drone yet!\nPlease try again after connecting to the drone")
        sock.close()
        sys.exit()

    #recvThread create
    recvThread = threading.Thread(target=recv)
    recvThread.start()

    print ('\r\n\r\nWelcome!\r\n')

    name_pliot = input("What is your name, pilot? ")
    print("Hello,",name_pliot +". Let's have some fun with the drone!\n")
    new_pilot = pilot(name_pliot)
    new_flight = flight()
    print ('\nPlease type "command" to start commanding the drone.\n')
    print ('Once the command interpreter returns "OK", type any command lines.\n')
    time.sleep(2)
    print ('\nIf need command instructions, type "help command".\n')
    print ('If you type something not in the command instruction, nothing will happen.\n')
    time.sleep(2)
    print ('\nIf want to disconnect, type "end".\n')
    time.sleep(2)

    while True:
        mode_select = input("Which mode do you want to use, automatic or manual?\nType either 'a' for automatic or 'm' for manual: ")

        if mode_select == 'a':
            print("\nYou selected 'automatic mode'! Please type 'command' to start.")
            while True:
                msg = input("")
                if  msg == "command":
                    msg = msg.encode(encoding="utf-8")
                    sent = sock.sendto(msg, tello_address)
                    break
                else:
                    print("please type 'command' first\n")

            while True:

                try:
                    # if drone_connected() == False:
                    #     print("\nSorry, it looks like you lost connection!\nPlease try again after connecting to the drone")
                    #     sock.close()
                    #     break

                    msg = input("")

                    if msg == "help command":
                        print(help_command())

                    if 'end' in msg:
                        # new_flight.battery_left()
                        # new_flight.flight_total()
                        print ('...')
                        sock.close()
                        break

                    # Send data
                    msg = msg.encode(encoding="utf-8")
                    sent = sock.sendto(msg, tello_address)

                    print("\nplease type any command lines.")

                except KeyboardInterrupt:
                    print ('\n . . .\n')
                    sock.close()
                    break

            print("I hope you enjoyed flying drone," + new_pilot.name)

            flight_metadata = {"Pilot_Name":new_pilot.name , "Flight_Note":None, 'Temp':None, 'Location':None, 'Time':new_flight.date}

            flightnote = input('If you want to record flight note, type here. If not, press enter. ')
            temperature = input('If you want to record the temperature(°F) right now, type here. If not, press enter. ')
            location = input('If you want to record the location where you flied drone, type here. If not, press enter. ')

            flight_metadata["Flight_Note"] = flightnote
            flight_metadata["Temp"] = temperature
            flight_metadata["Location"] = location

            ### DATABASE STORAGE ###

            conn = sqlite3.connect("Drone_Database.db")

            cur = conn.cursor()

            res = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
            table_list = cur.fetchall()
            if len(table_list) == 0:
                cur.execute('CREATE TABLE flight_metadata (Pilot_Name, Flight_Note, Temperature, Location, Date)')
            else:
                for table in table_list:
                    if 'flight_metadata' not in table:
                        cur.execute('CREATE TABLE flight_metadata (Pilot_Name, Flight_Note, Temperature, Location, Date)')

            values = tuple(flight_metadata.values())
            cur.execute('INSERT INTO flight_metadata values(?,?,?,?,?)', values)

            conn.commit()
            break

        elif mode_select == 'm':
            print("\nSorry, this mode is currently under development.")
            sock.close()
            break

        else:
            print("\nWrong command! Please Type again\n")

if __name__ == "__main__":
    main()
