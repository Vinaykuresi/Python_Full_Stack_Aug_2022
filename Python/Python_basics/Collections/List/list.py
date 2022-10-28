Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> emp_1 = "INF2021"
>>> emp_2 = "INF2022"
>>> emp_3 = "INF2023"
>>> 
>>> emp_list = ["INF2021", "INF2022", "INF2023", "INF2024", "INF2025" "INF2026"]
>>> emp_list[1]
'INF2022'
>>> emp_list_length = len(emp_list)
>>> emp_list_length
5
>>> len(emp_list)
5
>>> emp_list
['INF2021', 'INF2022', 'INF2023', 'INF2024', 'INF2025INF2026']
>>> emp_list = ["INF2021", "INF2022", "INF2023", "INF2024", "INF2025", "INF2026"]
>>> 
>>> emp_list_length = len(emp_list)
>>> emp_list_length
6
>>> emp_list[emp_list_length-1]
'INF2026'
>>> for emp_id in emp_list:
	print("Employee id : ", emp_id)

	
Employee id :  INF2021
Employee id :  INF2022
Employee id :  INF2023
Employee id :  INF2024
Employee id :  INF2025
Employee id :  INF2026
>>> 
>>> for index in range(emp_list_length):
	print("Employee id : ", emp_list[index])

	
Employee id :  INF2021
Employee id :  INF2022
Employee id :  INF2023
Employee id :  INF2024
Employee id :  INF2025
Employee id :  INF2026
>>>print("Hello")









