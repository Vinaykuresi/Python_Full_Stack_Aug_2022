
# from Employee_List import employeeDetails
from ..Employees import Employee_List
# from Employee_List import add_employee

flight_seats = 3

print(Employee_List.employeeDetails())

# add_employee("Roja")

# print(employeeDetails())

def increase_seats(no_of_seats):
    global flight_seats
    flight_seats += no_of_seats
    return flight_seats

def get_no_of_flight_seats():
    return flight_seats



