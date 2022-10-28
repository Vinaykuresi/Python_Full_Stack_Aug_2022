Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> range(4)
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]
>>> limit = 5
>>> list(range(1, limit+1))
[1, 2, 3, 4, 5]
>>> list(range(1, limit+1, -1))
[]
>>> list(range(limit+1, 1, -1))
[6, 5, 4, 3, 2]
>>> list(range(limit, 0, -1))
[5, 4, 3, 2, 1]
>>> 