Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> emp_list = ["INF2021", "INF2022", "INF2023", "INF2024", "INF2025" "INF2026"]
>>> 
>>> emp_list[5] = "INF2027"
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    emp_list[5] = "INF2027"
IndexError: list assignment index out of range
>>> emp_list = ["INF2021", "INF2022", "INF2023", "INF2024", "INF2025", "INF2026"]
>>> emp_list[5] = "INF2027"
>>> emp_list
['INF2021', 'INF2022', 'INF2023', 'INF2024', 'INF2025', 'INF2027']
>>> 
>>> emp_lists = [None] * 100
>>> emp_lists
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
>>> emp_lists = "INF20100"
>>> emp_lists
'INF20100'
>>> emp_lists = [None] * 100
>>> emp_lists[len(emp_lists)-1] = "INF20100"
>>> emp_lists
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'INF20100']
>>> [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'INF20100']
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'INF20100']
>>> # to know the length
>>> len(emp_lists)
100
>>> emp_list[3]
'INF2024'
>>> 
>>> 
>>> emp_list.append("INF2027")
>>> emp_list
['INF2021', 'INF2022', 'INF2023', 'INF2024', 'INF2025', 'INF2027', 'INF2027']
>>> 
>>> emp_list.pop()
'INF2027'
>>> emp_list
['INF2021', 'INF2022', 'INF2023', 'INF2024', 'INF2025', 'INF2027']
>>> ['INF2021', 'INF2022', 'INF2023', 'INF2024', 'INF2025', 'INF2027']
['INF2021', 'INF2022', 'INF2023', 'INF2024', 'INF2025', 'INF2027']
>>> emp_list.pop(2)
'INF2023'
>>> emp_list
['INF2021', 'INF2022', 'INF2024', 'INF2025', 'INF2027']
>>> final_list = emp_list + emp_lists
>>> final_list
['INF2021', 'INF2022', 'INF2024', 'INF2025', 'INF2027', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'INF20100']
>>> 