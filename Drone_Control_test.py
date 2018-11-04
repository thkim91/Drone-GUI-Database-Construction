from Drone_Control import *
import pytest

@pytest.fixture()
def object_instance():
    pilot1 = pilot('th')
    flight1 = flight(100)
    return [pilot1, flight1]

def test_name_of_pilot(object_instance):
    assert object_instance[0].name == 'th'

def test_battery_func_of_filght(object_instance):
    amount = 30 # Assuming that this is the amount of battery left(%)
    assert object_instance[1].battery_left(amount) == amount

def test_flight_time_func_of_filght(object_instance):
    amount = 60 # Assuming that this is the amount the drone flew in the unit of second
    assert object_instance[1].flight_total(amount) == amount

@pytest.mark.xfail(reason = 'The variable that is compared to flight.date is intentionally set to an incorrect date')
def test_date_flight(object_instance):
    random_date = date(2018,10,12)
    assert object_instance[1].date == random_date

def test_instruction_takeoff(help_command):
    "This function tests if there is an instruction for takeoff command"
    assert 'takeoff' in help_command

@pytest.mark.xfail(reason = 'It is not connected to drone network')
def test_internet_on():
    assert drone_connected == True
