from tkinter import *

ManWindow = None
mainProgram = None
root = None

def showManWindow():
    #mainProgram.destroy()
    ManWindow = Tk()
    #Label 1

    button5 = Button(ManWindow, text = 'Drone Takeoff')
    button5.pack() 
    button5.config(command = DroneTakeoff)

    button6 = Button(ManWindow, text = 'Drone Landing')
    button6.pack() 
    button6.config(command = DroneLanding)

    button7 = Button(ManWindow, text = 'Up')
    button7.pack() 
    button7.config(command = DroneUp)

    button8 = Button(ManWindow, text = 'Down')
    button8.pack() 
    button8.config(command = DroneDown)

    button9 = Button(ManWindow, text = 'Left')
    button9.pack() 
    button9.config(command = DroneLeft)

    button10 = Button(ManWindow, text = 'Right')
    button10.pack() 
    button10.config(command = DroneRight)
    
    button11 = Button(ManWindow, text = 'Turn Off')
    button11.pack() 
    button11.config(command = DroneOff)

    button12 = Button(ManWindow, text = 'Back')
    button12.pack() 
    button12.config(command = BackToPrevPage)
    
    button13 = Button(ManWindow, text = 'Battery: 100%')
    button13.pack() 

    ManWindow.geometry("200x250")
    ManWindow.mainloop()
                    
def showFlightSelectionPage():
    mainProgram = Tk()
    #Label 1

    button3 = Button(mainProgram, text = 'Choose Automatic Flight Plan')
    button3.pack() 
    button3.config(command = startAutomaticFlight)

    button4 = Button(mainProgram, text = 'Choose Manual Flight')
    button4.pack() 
    button4.config(command = showManWindow)
    mainProgram.geometry("200x120")
    mainProgram.mainloop()
    
def DroneTakeoff():
    pass

def DroneLanding():
    pass

def DroneUp():
    pass

def DroneOff():
    pass

def DroneDown():
    pass

def DroneDown():
    pass

def DroneLeft():
    pass

def DroneRight():
    pass

def BackToPrevPage():
    showFlightSelectionPage()

def startAutomaticFlight():
    pass

def login():
    possible_logins = [("root", "Abcd1234"), ("Test", "test")]
    username = entry1.get()
    password = entry2.get()
    for i in range(0, len(possible_logins)):
        if possible_logins[i][0] == username:
            if possible_logins[i][1] == password:  
                print("Login Successful")
                root.destroy();
                showFlightSelectionPage()
                return 0
            else:
                print("Incorrect password")
                return 0
    print("User was not found")
    
    
root = Tk()
root.geometry("200x120")
#Label 1
label1 = Label(root,text = 'Username')
label1.pack()
label1.config(justify = CENTER)

entry1 = Entry(root, width = 30)
entry1.pack()

label3 = Label(root, text="Password")
label3.pack()
label1.config(justify = CENTER)

entry2 = Entry(root, width = 30)
entry2.pack()

button1 = Button(root, text = 'Login!', bg="sky blue")
button1.pack() 