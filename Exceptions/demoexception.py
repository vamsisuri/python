from Exceptions.custexception import Myexception
try:
    age =int(input("Enter the age"))
    if age<18:
        raise Myexception("Invalid age")
except Myexception as e:
    print(e)
