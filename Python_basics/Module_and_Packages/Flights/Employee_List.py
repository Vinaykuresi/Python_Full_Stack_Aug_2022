from Flight_list import increase_seats, get_no_of_flight_seats 

employee_list = ["Vinay", "Kumar", "Radha"]

def add_employee(emp_name):
    global employee_list
    try:
        if(get_no_of_flight_seats() < len(employee_list)):
            increase_seats(len(employee_list) - get_no_of_flight_seats())
            print("Number of Seats : ", get_no_of_flight_seats(), " and no of passangers : ", len(employee_list))
            employee_list.append(emp_name)
            return "Employee details added successfully"
    except:
        return "Employee details added unSuccessfully"
    
def employeeDetails():
    return employee_list