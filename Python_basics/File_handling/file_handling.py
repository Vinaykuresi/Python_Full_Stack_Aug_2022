
from wsgiref.simple_server import demo_app


try : 
    demo_file = open("demo.txt",  "w")
    demo_file.write("Garuda Career Solutions.")

    demo_file = open("demo.txt",  "r")
    text = demo_file.read()

    print(text)
except:
    print("Error Occured")
finally:
    demo_file.close()
    if(demo_file.closed):
        print("File is Closed")
    else:
        print("File is not Closed")