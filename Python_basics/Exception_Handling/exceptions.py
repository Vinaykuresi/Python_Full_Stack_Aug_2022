
num = 10
total = num + int("20")
try:
    divisor = 5
    print(num/divisor)
    total = num + int("A")
    print(total)
except ZeroDivisionError:
    print("Shouldn't divide by Zero")
except TypeError:
    print("Integer shouldn't added with String")
except NameError:
    print("Please check the variable names")
except ValueError:
    print("Please check the Datatype conversion")
except:
    print("Some Error Has been Generated.")