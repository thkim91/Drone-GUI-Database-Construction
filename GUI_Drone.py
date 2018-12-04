from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import threading
import socket
import sys
import time
import pytest
from datetime import date
import sys
import sqlite3
import drone_prac as dp

from importlib import reload
reload(dp)


ManWindow = None
AutoWindow = None
InstructionPage = None
beforestartprogram = None
mainProgram = None
endFlight = None
DatabaseProgram = None 
root = None
endProgram = None
BGCOLOR = '#2095f5'


class showFlightSelectionPage():
	def __init__(self, master = None):
		self.mainProgram = Tk()
		#Label 1
		self.label0 = Label(mainProgram,text = 'Mode Selection')
		self.label0.config(background=BGCOLOR)
		self.label0.config(font=("Courier", 15))
		self.label0.pack()

		self.button3 = Button(mainProgram, text = 'Choose Automatic Flight Plan', command = self.AutoMode)
		self.button3.pack() 

		self.button4 = Button(mainProgram, text = 'Choose Manual Flight', command = self.ManualMode)
		self.button4.pack() 

		self.mainProgram.geometry("200x120")
		self.mainProgram.config(background=BGCOLOR)
		#mainProgram.mainloop()
	def AutoMode(self):
		self.mainProgram.destroy()
		showAutoWindow()
	def ManualMode(self):
		self.mainProgram.destroy()
		showManWindow()
    #self.mainProgram.mainloop()

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
    AutoWindow = Tk()
    
    def button_click():
        command2 = combo2.get()
        command3 = combo3.get()
        command4 = combo4.get()
        dp.Drone_Excecute("command,takeoff,"+command2+','+command3+','+command4+",land")
        AutoWindow.destroy()
        DoneFlight()
    
    str1 = StringVar()
    str2 = StringVar()
    str3 = StringVar()

    label1 = Label(AutoWindow,text = 'Control the Drone!')
    label1.grid(column = 0 , row = 0)

    label2 = Label(AutoWindow,text = 'Step1')
    label2.grid(column = 0 , row = 1)
    label3 = Label(AutoWindow,text = 'takeoff')
    label3.grid(column = 1 , row = 1)
    
    label4 = Label(AutoWindow,text = 'Step2')
    label4.grid(column = 0 , row = 2)
    combo2 = ttk.Combobox(AutoWindow, width=20, textvariable=str1)
    combo2['values'] = ('left 50' , 'right 50', 'flip r', 'cw 360')
    combo2.grid(column = 1 , row = 2)
    combo2.current(0)

    label5 = Label(AutoWindow,text = 'Step3')
    label5.grid(column = 0 , row = 3)
    combo3 = ttk.Combobox(AutoWindow, width=20, textvariable=str2)
    combo3['values'] = ('left 50' , 'right 50', 'flip r', 'cw 360')
    combo3.grid(column = 1 , row = 3)
    combo3.current(0)

    label6 = Label(AutoWindow,text = 'Step4')
    label6.grid(column = 0 , row = 4)
    combo4 = ttk.Combobox(AutoWindow, width=20, textvariable=str3)
    combo4['values'] = ('left 50' , 'right 50', 'flip r', 'cw 360')
    combo4.grid(column = 1 , row = 4)
    combo4.current(0)

    label7 = Label(AutoWindow,text = 'Step5')
    label7.grid(column = 0 , row = 5)
    label8 = Label(AutoWindow,text = 'land')
    label8.grid(column = 1 , row = 5 )

    action=Button(AutoWindow, text = 'OK', command = button_click)
    action.grid(column=0, row=6)

    AutoWindow.geometry("300x300")
    AutoWindow.config(background=BGCOLOR)
    AutoWindow.mainloop()

class showManWindow():
    def __init__(self, master = None):
        # mainProgram.destroy()
        self.ManWindow = Tk()

        #Label 1
        self.labelmw = Label(ManWindow,text = 'Control the Drone!')
        self.labelmw.config(background=BGCOLOR)

        self.labelmw.pack()
        self.labelmw.config(justify = CENTER)

        self.button5 = Button(ManWindow, text = 'Takeoff', command = DroneTakeoff)
        self.button5.pack() 

        self.button6 = Button(ManWindow, text = 'Land', command = DroneLanding)
        self.button6.pack() 

        self.button9 = Button(ManWindow, text = 'Left', command = DroneLeft)
        self.button9.pack() 

        self.button10 = Button(ManWindow, text = 'Right', command = DroneRight)
        self.button10.pack() 

        self.button11 = Button(ManWindow, text = 'Flip', command = DroneFlip)
        self.button11.pack()

        self.button12 = Button(ManWindow, text = 'Rotate', command = DroneRotate)
        self.button12.pack()

        self.button13 = Button(ManWindow, text = 'Instruction', command = showInstruction)
        self.button13.pack()

        self.button14 = Button(ManWindow, text = 'Done', command = self.close_DoneFlight)
        self.button14.pack()

        self.button12 = Button(ManWindow, text = 'Back', command = self.BackToPrevPage)
        self.button12.pack() 
        
        self.ManWindow.geometry("200x290")
        self.ManWindow.config(background=BGCOLOR)
        #ManWindow.mainloop()
    def BackToPrevPage(self):
        self.ManWindow.destroy()
        showFlightSelectionPage()
    def close_DoneFlight(self):
        self.ManWindow.destroy()
        DoneFlight()

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
    endProgram = Tk()

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
    dp.Drone_Excecute("left 50")

def DroneRight():
    dp.Drone_Excecute("right 50")

def DroneFlip():
    dp.Drone_Excecute("flip r")

def DroneRotate():
    dp.Drone_Excecute("cw 360")

#def BackToPrevPage():
    #showFlightSelectionPage()

def dataopen():
    DatabasePage()
    
def show_password():
    username = entry1.get()
    password = entry2.get()
    shown_password = (str(password))
    #time.sleep(1)
    visualize_password = Label(root, text = shown_password)
    visualize_password.pack()
    #time.sleep(1)
    #visualize_password.quit()

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

entry2 = Entry(root, show = '*', width = 30)
entry2.pack()

see_password = Button(root, text = 'see what you typed', bg = "red")
see_password.pack()
see_password.config(command = show_password)

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

# sock.close()