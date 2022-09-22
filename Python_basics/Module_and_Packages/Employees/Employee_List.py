
employee_list = ["Vinay", "Kumar", "Radha"]

def add_employee(emp_name):
    global employee_list
    try:
        employee_list.append(emp_name)
        return "Employee details added successfully"
    except:
        return "Employee details added unSuccessfully"
    
def employeeDetails():
    return employee_list