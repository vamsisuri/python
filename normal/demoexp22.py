from normal.demoexp1.py import Myexpection
try:
    age=int(input("Enter the age"))
    if age<18:
        raise Myexpection("Age is invalid")
    else:
        print(age)
except Myexception as e:
    print(e)