Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> not(not(not(False) or False))
True
>>> num_1 = 23
>>> num_2 = 32
>>> 
>>> num_3 = ((num_1 - num_1 )*1 + num_2%2)/2
>>> num_3
0.0
>>> 
>>> num_1 = True
>>> num_3 = 30
>>> ((num_1*3+10 <= num_3 % 2) <= False / True)) != True
SyntaxError: unmatched ')'
>>> ((num_1*3+10 <= num_3 % 2) <= False / True) != True
False
>>> 
>>> 30 > 40
False
>>> 43 >= 23
True
>>> True == False
False
>>> True != False
True
>>> num_3 += 23
>>> # num_3 = num_3 + 23
>>> num_3
53
>>> num_3 >= (num_3 %= 2)
SyntaxError: invalid syntax
>>> num_3 %= 2
>>> 53 >= (53%2)
True
>>> num_3 *= 23
>>> num_1*34 != (num_3%3 == 2)
True
>>> num_3
23
>>> True or False or False
True
>>> True*False and False or False
False
>>> num_2 = 10
>>> (((num_3+num_2) > 23/2) and (num_2 < num_3%3)) or (num_3 >= num_3 * 3)
False
>>> (((num_3+num_2) > 23/2) and (num_2 - num_3%3)) or (num_3 >= num_3 * 3)
8
>>> (((num2/num3) > 1) or (13-12)<12/3) and ((12+13)%5+10)-230
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    (((num2/num3) > 1) or (13-12)<12/3) and ((12+13)%5+10)-230
NameError: name 'num2' is not defined
>>> (((num_2/num_3) > 1) or (13-12)<12/3) and ((12+13)%5+10)-230
-220
>>> (10-9)*False+True and (32/4*True or 40%5)
8.0
>>> (10-9)*False+True
1
>>> (32/4*True or 40%5)
8.0
>>> 8 and 9
9
>>> 2 and 11
11
>>> 234 and 34
34
>>> 34 and 234
234
>>> 34 or 211
34
>>> 211 or 34
211
>>> 1 and 8
8
>>> 8 and 1
1
>>> 1 or 8
1
>>> 8 or 1
8
>>> 