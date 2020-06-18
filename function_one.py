#function
def prejwel():
    print("First Name is = Prejwel")
    print("Second name is = Harindran")
    return
prejwel()

#function with paramenter/arguments

def greeting(str):
    print("Hello",str+" You are learning Python")
    return
greeting("Prejwel")

#function with arguments (with all inputs not given , then 0/null should be there as input)
def details(name,email,phoneNum=0):
    print("Name=",name)
    print("Email=",email)
    print("phoneNumber=",phoneNum)
    return

details("prejwel","prej@gmail.com",)