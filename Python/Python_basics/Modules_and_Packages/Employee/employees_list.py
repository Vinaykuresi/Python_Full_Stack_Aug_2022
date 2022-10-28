
# first approach
# from ..Flights import flights_list

# second approach
import sys 
sys.path.append(r"C:\Users\Vinay Kuresi\Documents\Classes\Python_Full_Stack_Aug_2022\Python_basics\Modules_and_Packages\Flights")
import flights_list

employee_list = ["Vinay", "Kumar", "Radha"]

def add_employee(emp_names):
    global employee_list

    for emp in emp_names : 
        employee_list.append(emp)
        print(emp, " added to employee list successfully")

    print(flights_list.get_no_of_flight_seats())
    try:
        if(flights_list.get_no_of_flight_seats() < len(employee_list)):
            flights_list.increase_seats(len(employee_list) - flights_list.get_no_of_flight_seats())
            print("Number of Seats : ", flights_list.get_no_of_flight_seats(), " and no of passangers : ", len(employee_list))
    except:
        return "Employee details added unSuccessfully"
    
def employeeDetails():
    return employee_list

add_employee(["Suresh", "Divya", "Rakesh"])