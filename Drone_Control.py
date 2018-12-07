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
    # This function decodes the message that the drone sends to PC.
    # count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            # print(data.decode(encoding="utf-8"))
        except Exception:
            # print ('\nExit . . .\n')
            break

@pytest.fixture()
def drone_connected():
    # This function checks if the drone network is connected to the user's PC.
    # It compares the IP address the PC is getting with the actual drone's IP address.
    hostname = socket.gethostname()
    IPaddress = socket.gethostbyname(hostname)
    if IPaddress[0:10] == '192.168.10':
        return True
    else:
        return False

@pytest.fixture()
def help_command_man():
    # This function shows the instruction of all the commands for the drone.
    instruction = """
    Here are the commands that you can use:
    (The length of distance the drone move each time is fixed to 50cm.)
    1. Takeoff: Drone will takeoff.
    2. Land: Drone will land.
    3. Left: Drone will move to the left.
    4. Right: Drone will move to the right.
    5. Flip: Drone will flip to the right.
    6. Rotate: Drone will do the clockwise rotation 360 degree.
    """
    return instruction

@pytest.fixture()
def help_command_auto():
    instruction = """
    1. left 50: Drone will move 50cm to the left.
    2. right 50: Drone will move 50cm to the right.
    3. flip r: Drone will flip to the right.
    4. cw 360: Drone will do clockwise rotation 360 degree.
    """
    return instruction

def Drone_Start(msg):
    if msg == "command":
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, tello_address)
        return True
    else:
        # print("\nWrong command!")
        return False

def Drone_Excecute(command):
    msg_list = command.split(',')
    for msg in msg_list:
        try:
            msg = msg.encode(encoding="utf-8")
            sent = sock.sendto(msg, tello_address)
            time.sleep(5)
        except KeyboardInterrupt:
            # print ('\n . . .\n')
            sock.close()

def Drone_end():
    sock.close()

def Record_Database(pilot_name = None, flightnote = None, temperature = None, location = None, flight_date = None):
    ### DATABASE STORAGE ###
    # We used database called SQlite3 to save the info.
    conn = sqlite3.connect("Drone_Database.db")

    cur = conn.cursor()

    res = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_list = cur.fetchall()
    # Fisrt, the table will be made if there is no table.
    # There are five attributes in the table for now, but there may be more later on.
    if len(table_list) == 0:
        cur.execute('CREATE TABLE flight_metadata (Pilot_Name, Flight_Note, Temperature, Location, Date)')
    else:
        for table in table_list:
            if 'flight_metadata' not in table:
                cur.execute('CREATE TABLE flight_metadata (Pilot_Name, Flight_Note, Temperature, Location, Date)')

    values = (pilot_name, flightnote, temperature, location, flight_date)
    # Then the info will be inserted into the table.
    cur.execute('INSERT INTO flight_metadata values(?,?,?,?,?)', values)

    conn.commit()

    cur.execute("SELECT * FROM flight_metadata")
    return cur.fetchall()

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
