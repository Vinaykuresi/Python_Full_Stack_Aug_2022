Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num_1 = 20
>>> num_2 = 10
>>> num_3 = 30
>>> 
>>> num_1 = num_1 % num_3
>>> num_1
20
>>> num_1 = num_3 / num_1 - 5
>>> num_1
-3.5
>>> 
>>> num_1 = num_1 * 2 - num_3
>>> num_1
-37.0
>>> num_1 = num_1 + num_2 - num_1 * 20 % 5
>>> num_1 = num_1 + num_2 - (num_1 * 20) % 5 % num_3
>>> num_1
-17.0
>>> num_1 = -37.0
>>> num_1 = num_1 + num_2 - num_1 * 20 % 5
>>> num_1
-27.0
>>> 2020 > 2020
False
>>> (2020 > 2020) < True
True
>>> num_1+42 == num_3/2 > False
True
>>> ((10*20)%3 == num_3*2) > True < False <= False
False
\
>>> ((10*20)%3 == num_3*2)
False
>>> False > True < False <= False
False
>>> False <= False
True
>>> False > True < True
False
>>> num_1 = num_2*3/1.5 != 4 < - num_3%3 > 3
>>> num_1 > False
False
>>> 
>>> 
>>> num_1*3+10 >= num_3 - 20 <= Ture * False != False
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    num_1*3+10 >= num_3 - 20 <= Ture * False != False
NameError: name 'Ture' is not defined
>>> num_1*3+10 >= num_3 - 20 <= True * False != False
False
>>> True * False != False
False
>>> 10 <= False
False
>>> 10 >= False
True
>>> num_1*3+10
10
>>> True * False
0
>>> 0 != False
False
>>> num_3
30
>>> num_1*3+10 >= num_3 - 20
True
>>> True <= False
False
>>> num_1 = True
>>> (num_1*3+10 >= num_3 - 2 <= False * False != True) > True > num_2
False
>>> (num_1*3+10 >= num_3 - 2 <= False * False != True)
False
>>> False * False != True
True
>>> num_1*3+10
13
>>> num_3 - 2
28
>>> num_1*3+10 >= num_3 - 2
False
>>> (num_1*3+10 >= num_3 - 2) <= False * False != True
True
>>> num_1*3+10 >= num_3 - 2 <= False * False != True
False
>>> (num_1*3+10 >= num_3 - 2 <= False) * (False != True)
0
>>> num_1*3+10 >= num_3 - 2 <= False*False != True
False
>>> (num_1*3+10 >= num_3 - 2 <= False * False) != True
True
>>> num_1*3+10 >= num_3 - 2 <= False * False != True
False
>>> False * False
0
>>> num_1*3+10 >= num_3 - 2 <= (False * False) != True
False
>>> (num_1*3+10 >= num_3 - 2 <= (False * False) != True) > True > num_2
False
>>> (True*num_1*3+10 >= num_3 - 2 <= False * True != False) > True > num_2 != (True*True)%1