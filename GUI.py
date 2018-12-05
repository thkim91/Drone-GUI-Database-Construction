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
import Drone_Control as dp

from importlib import reload
reload(dp)

BGCOLOR = '#2095f5'

def showFlightSelectionPage(username):
    mainProgram = Tk()

    def button_auto():
        mainProgram.destroy()
        showAutoWindow(username)
    def button_man():
        mainProgram.destroy()
        showManWindow(username)

    label0 = Label(mainProgram,text = 'Mode Selection')
    label0.config(background=BGCOLOR,font=("Courier", 15))
    label0.pack()

    button3 = Button(mainProgram, text = 'Choose Automatic Flight Plan',width=25, command = button_auto)
    button3.pack()

    button4 = Button(mainProgram, text = 'Choose Manual Flight',width=25, command = button_man)
    button4.pack()

    mainProgram.geometry("200x120")
    mainProgram.config(background=BGCOLOR)
    mainProgram.mainloop()

def BeforeStart():
    beforestartprogram = Tk()

    def button_click():
        beforestartprogram.destroy()
        StartProgram()

    label1 = Label(beforestartprogram,text = 'Select Command to start!')
    label1.config(background=BGCOLOR,font=("Courier", 10))
    label1.pack()

    button1 = Button(beforestartprogram, text = 'Command', command = button_click)
    button1.pack()

    beforestartprogram.geometry("300x120")
    beforestartprogram.config(background=BGCOLOR)
    beforestartprogram.mainloop()

def showAutoWindow(username):
    AutoWindow = Tk()

    def button_command():
        command2 = combo2.get()
        command3 = combo3.get()
        command4 = combo4.get()
        # dp.Drone_Excecute("command,takeoff,"+command2+','+command3+','+command4+",land")

    def button_done():
        AutoWindow.destroy()
        DoneFlight(username)
    def button_back():
        AutoWindow.destroy()
        showFlightSelectionPage(username)

    str1 = StringVar()
    str2 = StringVar()
    str3 = StringVar()

    label1 = Label(AutoWindow,text = 'Control the Drone!')
    label1.config(background=BGCOLOR)
    label1.grid(column = 0 , row = 0)

    label2 = Label(AutoWindow,text = 'Step1')
    label2.config(background=BGCOLOR)
    label2.grid(column = 0 , row = 1)
    label3 = Label(AutoWindow,width=22,text = 'takeoff')
    label3.grid(column = 1 , row = 1)

    label4 = Label(AutoWindow,text = 'Step2')
    label4.config(background=BGCOLOR)
    label4.grid(column = 0 , row = 2)
    combo2 = ttk.Combobox(AutoWindow, width=20, textvariable=str1)
    combo2['values'] = ('left 50' , 'right 50', 'flip r', 'cw 360')
    combo2.grid(column = 1 , row = 2)
    combo2.current(0)

    label5 = Label(AutoWindow,text = 'Step3')
    label5.config(background=BGCOLOR)
    label5.grid(column = 0 , row = 3)
    combo3 = ttk.Combobox(AutoWindow, width=20, textvariable=str2)
    combo3['values'] = ('left 50' , 'right 50', 'flip r', 'cw 360')
    combo3.grid(column = 1 , row = 3)
    combo3.current(0)

    label6 = Label(AutoWindow,text = 'Step4')
    label6.config(background=BGCOLOR)
    label6.grid(column = 0 , row = 4)
    combo4 = ttk.Combobox(AutoWindow, width=20, textvariable=str3)
    combo4['values'] = ('left 50' , 'right 50', 'flip r', 'cw 360')
    combo4.grid(column = 1 , row = 4)
    combo4.current(0)

    label7 = Label(AutoWindow,text = 'Step5')
    label7.config(background=BGCOLOR)
    label7.grid(column = 0 , row = 5)
    label8 = Label(AutoWindow,width=22,text = 'land')
    label8.grid(column = 1 , row = 5 )

    action=Button(AutoWindow, text = 'OK',width=10, command = button_command)
    action.grid(column=1, row=7)
    button1= Button(AutoWindow, text = 'Done',width=10, command = button_done)
    button1.grid(column=1, row=9)
    button2 = Button(AutoWindow, text = 'Back',width=10, command = button_back)
    button2.grid(column=1, row=10)

    AutoWindow.geometry("300x300")
    AutoWindow.config(background=BGCOLOR)
    AutoWindow.mainloop()

def showManWindow(username):
    ManWindow = Tk()

    def button_done():
        ManWindow.destroy()
        DoneFlight(username)

    def button_back():
        ManWindow.destroy()
        showFlightSelectionPage(username)

    labelmw = Label(ManWindow,text = 'Control the Drone!')
    labelmw.config(background=BGCOLOR)

    labelmw.pack()
    labelmw.config(justify = CENTER)

    button5 = Button(ManWindow, text = 'Takeoff',width=20, command = DroneTakeoff)
    button5.pack()

    button6 = Button(ManWindow, text = 'Land',width=20, command = DroneLanding)
    button6.pack()

    button9 = Button(ManWindow, text = 'Left',width=20, command = DroneLeft)
    button9.pack()

    button10 = Button(ManWindow, text = 'Right',width=20, command = DroneRight)
    button10.pack()

    button11 = Button(ManWindow, text = 'Flip',width=20, command = DroneFlip)
    button11.pack()

    button12 = Button(ManWindow, text = 'Rotate',width=20, command = DroneRotate)
    button12.pack()

    button13 = Button(ManWindow, text = 'Instruction',width=20, command = showInstruction)
    button13.pack()

    button14 = Button(ManWindow, text = 'Done',width=10, command = button_done)
    button14.pack()

    button12 = Button(ManWindow, text = 'Back',width=10, command = button_back)
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

def DoneFlight(username):
    endFlight = Tk()

    def button_database():
        endFlight.destroy()
        DatabasePage(username)

    label1 = Label(endFlight,text = 'Hope you enjoyed the flight!')
    label1.config(background=BGCOLOR,justify = CENTER,font=("Courier", 12))
    label1.pack()

    button1 = Button(endFlight, text = 'Click to Record Info', command = button_database)
    button1.pack()

    endFlight.geometry("360x120")
    endFlight.config(background=BGCOLOR)
    endFlight.mainloop()

def DatabasePage(username):
    DatabaseProgram = Tk()
    def button_record():
        note = entry11.get()
        temp = entry12.get()
        loca = entry13.get()
        dp.Record_Database(username,note,temp,loca,date.today())
        DatabaseProgram.destroy()
        DoneProgram()

    label1 = Label(DatabaseProgram,font = 12, text="Record the following:")
    label1.grid(row = 0, column = 0)

    label2 = Label(DatabaseProgram, text="Pilot Name")
    label2.grid(row = 1, column = 0)
    label3 = Label(DatabaseProgram, text=username)
    label3.grid(row = 1, column = 1)

    label4 = Label(DatabaseProgram, text="Flight Note")
    label4.grid(row = 2, column = 0)
    entry11 = Entry(DatabaseProgram)
    entry11.grid(row = 2, column = 1)

    label5 = Label(DatabaseProgram, text="Temperature")
    label5.grid(row = 3, column = 0)
    entry12 = Entry(DatabaseProgram)
    entry12.grid(row = 3, column = 1)

    label6 = Label(DatabaseProgram, text="Location")
    label6.grid(row = 4, column = 0)
    entry13 = Entry(DatabaseProgram)
    entry13.grid(row = 4, column = 1)

    label7 = Label(DatabaseProgram, text="Flight Date")
    label7.grid(row = 5, column = 0)
    label8 = Label(DatabaseProgram, text=date.today())
    label8.grid(row = 5, column = 1)

    button1 = Button(DatabaseProgram, text="OK", width=15, command = button_record)
    button1.grid(row=6,column=1)
    DatabaseProgram.mainloop()

def DoneProgram():
    endProgram = Tk()

    label1 = Label(endProgram,text = 'Thank you!')
    label1.config(background=BGCOLOR, font=("Courier",20))
    label1.pack()

    endProgram.geometry("200x100")
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

###############################

def login():
    possible_logins = [("Test", "test"),("Taehoon","taehoon"),("Bill","bill"),("Charidy","charidy"),("Siyu","siyu")]
    username = entry1.get()
    password = entry2.get()
    for i in range(0, len(possible_logins)):
        if possible_logins[i][0] == username:
            if possible_logins[i][1] == password:
                # if dp.drone_connected():
                print("Login Successful")
                root.destroy()
                showFlightSelectionPage(username)
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
label0.config(justify = CENTER,font=("Courier", 15))

label1 = Label(root,text = 'Username')
label1.config(background=BGCOLOR)

label1.pack()
label1.config(justify = CENTER)

entry1 = Entry(root, width = 30)
entry1.pack()

label3 = Label(root, text="Password")
label3.config(background=BGCOLOR)
label3.pack()

entry2 = Entry(root, show = '*', width = 30)
entry2.pack()

button1 = Button(root, text = 'Login', bg="sky blue", command = login)
button1.pack()

root.mainloop()

# sock.close()
