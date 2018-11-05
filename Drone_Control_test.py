from Drone_Control import *
import pytest

@pytest.fixture()
def object_instance():
    pilot1 = pilot('th')
    flight1 = flight()
    return [pilot1, flight1]

# Check to see if the Pilot's name is saved correctly
def test_name_of_pilot(object_instance):
    assert object_instance[0].name == 'th'

# Check to see if the battery life is saved correctly
def test_battery_func_of_flight(object_instance):
    amount = 30 # Assuming that this is the amount of battery left(%)
    assert object_instance[1].battery_left(amount) == amount

# Check to see if the flight time is saved correctly
def test_flight_time_func_of_flight(object_instance):
    amount = 60 # Assuming that this is the amount the drone flew in the unit of second
    assert object_instance[1].flight_total(amount) == amount

# Check to see if the flight date is today's date
@pytest.mark.xfail(reason = 'The variable that is compared to flight.date is intentionally set to an incorrect date')
def test_date_flight(object_instance):
    random_date = date(2018,10,12)
    assert object_instance[1].date == random_date

# Check if the takeoff command is contained in the help_command
def test_instruction_takeoff(help_command):
    "This function tests if there is an instruction for takeoff command"
    assert 'takeoff' in help_command

# Check to see if we are connected to the drone
@pytest.mark.xfail(reason = 'It is not connected to drone network')
def test_drone_connected(drone_connected):
    assert drone_connected == True

