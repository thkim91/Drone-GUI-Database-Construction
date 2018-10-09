# Part A, B
* The document below covers Part A and B

# IST_303-GroupProject--Group2
* IST 303 Group 2 - The Python Pilots

# Concept
* Control the Tello drone with a GUI to take off, fly, and land.

# Requirements - User stories
* Title: Take off
  * Description: As a user, I should be able to launch the drone from the ground into the air, so that I can begin a flight route.
  * Completion time: One week
  * Priority: 10
  * Tasks:
    * Create a command to connect with the drone (7 hours)
    * Create a Flight class (12 hours)
    * Create a Flight object in the datastore (12 hours)

* Title: Land drone
  * Description: As a user, I should be able to land the drone safely on the ground, so that I can end the flight without damaging the drone.
  * Completion time: One week
  * Priority: 10
  * Tasks:
    * Program the code for landing (31 hours)
      * Create a command to initiate landing (12 hours)
      * Stop drone after successful landing (12 hours)
    * Return status message [successful landing, unsuccessful landing] (7 hours)

* Title: Choose flight mode 
  * Description: As a user, I should be able to choose the flight mode (manual control or flight plan) so that I can fly the drone in two different ways.
  * Completion time: One week
  * Priority: 20
  * Tasks:
    * Create a command to receive user input for flight mode (manual or automatic) (12 hours)

* Title: Fly drone in manual mode
  * Description: As a user, I should be able to control the drone’s movement in real time so that I can improvise the flight path.
  * Completion time: Two weeks
  * Priority: 10
  * Tasks:
    * Create commands to receive user input for flight direction, distance, and speed. (20 hours)
    * Create commands to send user input to drone for execution (20 hours)

* Title: Display the remaining charge of the battery.
  * Description: As a user, I should be able to see the remaining battery charge in the GUI.
  * Completion time: One week
  * Priority: 30
  * Tasks:
    * Create a command to request the battery charge level (12 hours)
    * Create a return message which prints the battery charge level to the screen (12 hours)

* Title: Display the drone’s status
  * Description: As a user, I should be able to see the connection status of the drone. For example, if the drone is either connected or disconnected from the computer.
  * Completion time: One week
  * Priority: 30
  * Tasks:
    * Create a command to request the drone’s status. (6 hours)
    * Create a return message which prints the connection status (drone is connected or disconnected). (18 hours)

* Title: Define flight plan
  * Description: As a user, I should be able to design a flight plan in the GUI and have the drone execute the flight plan so that I can fly the drone automatically.
  * Completion time: 2 weeks
  * Priority: 20
  * Tasks:
    * Create a Flight Plan class (8 hours)
    * Accept user input for Flight Plan (8 hours)
    * Create Flight Plan object (8 hours)
    * Execute Flight Plan object (16 hours)
    * Convert user input into executable instructions (16 hours)
    * Example test case: Execute and test a flight plan in a square (8 hours)

* Title: Record flight metadata
  * Description: As a user, I should be able to write flight notes after a flight so that I can have a record for flights for reference (e.g. debugging)
  * Completion time: 1 week
  * Priority: 30
  * Tasks:
    * Create a command to accept user input for flight notes (11 hours)
    * Create a command to accept user input for temperature during flight (11 hours)
    * Create a command to accept user input for pilot name after flight (11 hours)
    * Save flight notes, temperature, and pilot name as a part of the Flight object (17 hours)


# Stakeholders
* Farmers - check crops
  * As a farmer, I want plan a flight route, to check my crops.

* Landscape architects - help design
  * As a landscape, I want to take photos of the site, to help design the landscape.

* Mining planner - check progress of mining
  * As a mining planner, what I want is the geographical characteristics of particular areas like longitude and latitude.

* People in the travel industry or real estate - plan aerial shots of a location
  * As a travel blogger, I want to post aerial photographs of my travel locations to my website and social media platforms

* Toy store - let users use a simple UI to control the drone
  * As a player, I want fly drone in a circle because I think it’s cool.
  
* Sell software to people that don’t have a suitable phone to control it

# Data elements (flight log)
* Flight ID
* Flight time
* Pilot ID
* Date
* Distance
* Source location
* Destination location
* Complete flight? [True/False]
* Reason for the failure, if applicable
* Temperature
* #of charges
* Location of charge

# Allocation
* Please check our trello website (https://trello.com/b/BYz9KJnR/drone-gui-program)

# Burn-Down Chart
* Velocity:
  * Numerator: 8 hours/person/week 
  * Denominator: 3 days * 8 hours/day = 24 hours/person/week  (Since 3 days are the possible working days per week)
  * Velocity : 1/3

# GitHub
* GitHub repository: https://github.com/thkim91/IST_303-GroupProject--Group2.git

# Team members
* Taehoon Kim
  * Phone #: 909 543 8810
  * Email address: th.kim9112@gmail.com
* Charidy Paige
  * Phone #: 205.332-4191
  * Email address:mecpaige@gmail.com
* Bill Pepper
  * Phone #: 818 793 3384
  * Email address: williamepepper@gmail.com
* Siyu Xiang
  * Phone #:
  * Email address:siyu7866@gmail.com

# Team meetings
* 9/26/201
  * Attendees: Taehoon, Charidy, Bill, & Siyu
  * Notes:
    * Discussed project concept and user stories
    * Collaboratively created new user stores (e.g. flight plan)
    * Scheduling time to meet with Prof. Chipidza on project scope
* 09/27/2018
  * Attendees: Taehoon, Charidy, Bill, Siyu, & Prof. Chipidza
  * Notes:
    * Identify stakeholders
    * Identify different kinds of users
    * New user stories:
      * Change the password, should be able to access.
    * Determine reports
    * Consider the feasibility of the project
    * You can change it to normal airline company if drone does not work
* 10/07/2018
  * Attendees: Taehoon,Bill, & Siyu
  * Notes:
    * Added user stories
    * Divide user stories into tasks
    * Allocated the tasks
    * Velocity Calculations & Burndown charts
    * Tried to send command to Drone 

# References
* https://www.ryzerobotics.com/tello
* https://dl-cdn.ryzerobotics.com/downloads/tello/0228/Tello+SDK+Readme.pdf
