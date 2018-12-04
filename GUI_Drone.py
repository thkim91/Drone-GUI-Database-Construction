from tkinter import *
from tkinter import messagebox
import threading
import socket
import sys
import time
import pytest
from datetime import date
import sys
import sqlite3
import drone_prac as dp
import tkinter

from importlib import reload
reload(dp)

# host = ''
# port = 9000
# locaddr = (host,port)

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# tello_address = ('192.168.10.1', 8889)

# sock.bind(locaddr)

# recvThread = threading.Thread(target=recv)
# recvThread.start()

ManWindow = None
AutoWindow = None
InstructionPage = None
beforestartprogram = None
mainProgram = None
endFlight = None
DatabaseProgram = None 
root = None
endProgram = None
Closewindow = False
BGCOLOR = '#2095f5'
evalue = 0

#class flight_page():
    #def __init__():
        #pass
class showFlightSelectionPage():

   #selection = button3.get()
    def __init__(self,master = None):
        self.mainProgram = Tk()
        self.label0 = Label(mainProgram,text = 'Mode Selection')
        self.label0.config(background=BGCOLOR)
        self.label0.config(font=("Courier", 15))
        self.label0.pack()

        self.button3 = Button(mainProgram, text = 'Choose Automatic Flight Plan', command = self.AutoMode)
        self.button3.pack() 

        self.button4 = Button(mainProgram, text = 'Choose Manual Flight', command = self.ManualMode)
        self.button4.pack()

        #self.button5 = Button(mainProgram, text = 'Go', command = self.closemainProgram)
        #self.button5.pack()


        self.mainProgram.geometry("200x120")
        self.mainProgram.config(background=BGCOLOR)
    def AutoMode(self):
        self.mainProgram.destroy()
        showAutoWindow()
    def ManualMode(self):
        self.mainProgram.destroy()
        showManWindow()
    '''def create_window():
       #mainProgram = Tk()
        frame = Frame(mainProgram)
        frame.pack()
        v = tkinter.IntVar()
        v.set(1)'''
        #Label 1
'''label0 = Label(mainProgram,text = 'Mode Selection')
        label0.config(background=BGCOLOR)
        label0.config(font=("Courier", 15))
        label0.pack()

        button3 = Radiobutton(frame, text = 'Choose Automatic Flight Plan',variable = v, value = 1, command = showAutoWindow)
        button3.pack() 

        button4 = Radiobutton(mainProgram, text = 'Choose Manual Flight', variable = v, value = 2, command = BeforeStart)
        button4.pack()

        button5 = Button(frame, text = 'Go', command = self.closemainProgram)
        button5.pack()


        mainProgram.geometry("200x120")
        mainProgram.config(background=BGCOLOR)
        mainProgram.mainloop()'''

def BeforeStart():
    beforestartprogram = Tk()

    label1 = Label(beforestartprogram,text = 'Select Command to start!')
    label1.config(background=BGCOLOR)
    label1.config(font=("Courier", 10))  
    label1.pack()    

    button1 = Button(beforestartprogram, text = 'Command', command = StartProgram)
    button1.pack()
    
    beforestartprogram.geometry("300x120")
    beforestartprogram.config(background=BGCOLOR)
    beforestartprogram.mainloop()

def showAutoWindow():
    #showFlightSelectionPage == 1:

    #showFlightSelectionPage.Tk().destroy()
    AutoWindow = Tk()
    label1 = Label(AutoWindow,text = 'Sorry, it is currently under development!')
    label1.config(background=BGCOLOR)
    label1.config(font=("Courier", 12))  
    label1.pack()    
    
    AutoWindow.geometry("500x100")
    AutoWindow.config(background=BGCOLOR)
    AutoWindow.mainloop()

def showManWindow():
    # mainProgram.destroy()
    ManWindow = Tk()

    #Label 1
    labelmw = Label(ManWindow,text = 'Control the Drone!')
    labelmw.config(background=BGCOLOR)

    labelmw.pack()
    labelmw.config(justify = CENTER)

    button5 = Button(ManWindow, text = 'Drone Takeoff', command = DroneTakeoff)
    button5.pack() 

    button6 = Button(ManWindow, text = 'Drone Landing', command = DroneLanding)
    button6.pack() 

    button9 = Button(ManWindow, text = 'Left', command = DroneLeft)
    button9.pack() 

    button10 = Button(ManWindow, text = 'Right', command = DroneRight)
    button10.pack() 

    button13 = Button(ManWindow, text = 'Instruction', command = showInstruction)
    button13.pack()

    button14 = Button(ManWindow, text = 'Done', command = DoneFlight)
    button14.pack()

    button12 = Button(ManWindow, text = 'Back', command = BackToPrevPage)
    button12.pack() 
    
    ManWindow.geometry("200x290")
    ManWindow.config(background=BGCOLOR)
    ManWindow.mainloop()

def showInstruction():
    InstructionPage = Tk()

    label1 = Label(InstructionPage,text = dp.help_command(),justify="left")
    label1.config(background=BGCOLOR)
    label1.config(font=("Courier", 12))  
    label1.pack()
    
    InstructionPage.geometry("720x540")
    InstructionPage.config(background=BGCOLOR)    
    InstructionPage.mainloop()

def DoneFlight():
    # socket.close()
    endFlight = Tk()

    label1 = Label(endFlight,text = 'Hope you enjoyed the flight!')
    label1.config(background=BGCOLOR)
    label1.config(justify = CENTER)
    label1.config(font=("Courier", 12))  
    label1.pack()    

    button1 = Button(endFlight, text = 'Click to Record Info', command = endFlight.destroy)
    button1.pack()

    endFlight.geometry("360x120")
    endFlight.config(background=BGCOLOR)
    endFlight.mainloop()


def DoneProgram():
    # socket.close()
    endProgram = Tk()

    # dp.Record_Database(username)

    label1 = Label(endProgram,text = 'Thank you!')
    label1.config(background=BGCOLOR)
    label1.config(justify = CENTER)
    label1.config(font=("Courier", 12))  
    label1.pack()    

    endProgram.geometry("160x120")
    endProgram.config(background=BGCOLOR)
    endProgram.mainloop()

#### Functions ####
def StartProgram():
    dp.Drone_Start("command")
    showManWindow()

def DroneTakeoff():
    dp.Drone_Excecute("takeoff")

def DroneLanding():
    dp.Drone_Excecute("land")

def DroneLeft():
    pass

def DroneRight():
    pass

def BackToPrevPage():
    showFlightSelectionPage()

def dataopen():
    DatabasePage()

###############################

def login():
    possible_logins = [("root", "Abcd1234"), ("Test", "test")]
    username = entry1.get()
    password = entry2.get()
    for i in range(0, len(possible_logins)):
        if possible_logins[i][0] == username:
            if possible_logins[i][1] == password:
                # if dp.drone_connected():  
                print("Login Successful")
                root.destroy();
                showFlightSelectionPage()
                return 0
                # else:
                #     messagebox.showerror("Error", "Drone is not connected!")
            else:
                messagebox.showerror("Error","Incorrect password")
                return 0
        
    messagebox.showerror("Error","User was not found")


root = Tk()
root.config(background=BGCOLOR)
root.geometry("200x150")

label0 = Label(root,text = 'Python Pilots')
label0.config(background=BGCOLOR)

label0.pack()
label0.config(justify = CENTER)
label0.config(font=("Courier", 15))

label1 = Label(root,text = 'Username')
label1.config(background=BGCOLOR)

label1.pack()
label1.config(justify = CENTER)

entry1 = Entry(root, width = 30)
entry1.pack()

label3 = Label(root, text="Password")
label3.config(background=BGCOLOR)
label3.pack()
label1.config(justify = CENTER)

entry2 = Entry(root, width = 30)
entry2.pack()

button1 = Button(root, text = 'Login', bg="sky blue", command = login)
button1.pack() 

root.mainloop()

def DatabasePage():
    #pilot_name, flightnote, temperature, location, flight_date
    name = entry10.get()
    note = entry11.get()
    temp = entry12.get()
    loca = entry13.get()
    dp.Record_Database(name,note,temp,loca,date.today())
    DatabaseProgram.destroy()
    DoneProgram()

DatabaseProgram = Tk()

label10 = Label(DatabaseProgram, text="Pilot Name")
label10.grid(row = 0, column = 0)


# label100 = Label(DatabaseProgram, text="username")
# label100.grid(row = 0, column = 1)
entry10 = Entry(DatabaseProgram)
entry10.grid(row = 0, column = 1)

label11 = Label(DatabaseProgram, text="Flight Note")
label11.grid(row = 1, column = 0)
entry11 = Entry(DatabaseProgram)
entry11.grid(row = 1, column = 1)

label12 = Label(DatabaseProgram, text="Temperature")
label12.grid(row = 2, column = 0)
entry12 = Entry(DatabaseProgram)
entry12.grid(row = 2, column = 1)

label13 = Label(DatabaseProgram, text="Location")
label13.grid(row = 3, column = 0)

entry13 = Entry(DatabaseProgram)
entry13.grid(row = 3, column = 1)

label14 = Label(DatabaseProgram, text="Flight Date")
label14.grid(row = 4, column = 0)

label140 = Label(DatabaseProgram, text=date.today())
label140.grid(row = 4, column = 1)

button1 = Button(DatabaseProgram, text="OK", width=15, command = DatabasePage)
button1.grid(row=5,column=1)
DatabaseProgram.mainloop()

