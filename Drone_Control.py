# Tello Python3 Control Demo 
# http://www.ryzerobotics.com/

import threading 
import socket
import sys
import time
import pytest

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

def internet_on():    
    hostname = socket.gethostname()
    IPaddress = socket.gethostbyname(hostname)
    if IPaddress == tello_address[0]:
        return True
    else:
        return False
    
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
        - Speed?  : shows current speed
        - Battery? : shows current battery percentage
        - Time? : shows current flight time
    """
    return instruction

class pilot():
    count = 0
    def __init__(self,name):
        self.name = name
        pilot.count += 1

from datetime import date
class flight():
    date = date.today()
    def __init__(self,battery,flight_time=0):
        self.battery = battery
        self.flight_time = flight_time
    def battery_left(self,amount):
        self.battery -= amount
        return self.battery
    def flight_total(self,amount):
        self.flight_time += amount
        return self.flight_time


##### Testing Begins #####

@pytest.fixture()
def object_instance():
    pilot1 = pilot('th')
    flight1 = flight(100)
    return [pilot1, flight1]

def test_name_of_pilot(object_instance):
    assert object_instance[0].name == 'th'

def test_battery_func_of_filght(object_instance):
    amount = 30
    assert object_instance[1].battery_left(amount) == 100 - amount

@pytest.mark.xfail(reason = 'The variable that is compared to flight.date is intentionally set to an incorrect date')
def test_date_flight(object_instance):
    random_date = date(2018,10,12)
    assert object_instance[1].date == random_date

def test_instruction_takeoff(help_command):
    "This function tests if there is an instruction for takeoff command"
    assert 'takeoff' in help_command

@pytest.mark.xfail(reason = 'It is not connected to drone ip')
def test_internet_on():
    assert internet_on == True

##### Testing ends #####


def main():
    #recvThread create
    recvThread = threading.Thread(target=recv)
    recvThread.start()
    
    print ('\r\n\r\nWelcome!\r\n')

    name_pliot = input("What is your name, pilot?")
    print("Hello,",name_pliot +". Let's have some fun with the drone!\n")
    new_flight = flight(name_pliot)
    print ('\nPlease type "command" to start commanding the drone.\n')
    print ('Once the command interpreter returns "OK", type any command lines.\n')
    print ('If need command instructions, type "help command".\n')
    print ('If want to disconnect, type "end".\n')

    while True: 

        try:
            if internet_on() == False:
                print("\nSorry, it looks like you have not successfully connected to drone yet!\nPlease try again after connecting to the drone")
                sock.close() 
                break
            else:
                pass
                
            msg = input("")
                
            if not msg:
                break  
            
            if msg == "help command":
                print(help_command())

            if 'end' in msg:
                print ('...')
                sock.close()  
                break

            
            # Send data
            msg = msg.encode(encoding="utf-8") 
            sent = sock.sendto(msg, tello_address)
        
        except KeyboardInterrupt:
            print ('\n . . .\n')
            sock.close()  
            break


if __name__ == "__main__":
    main()


