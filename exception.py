#TODO EXCEPTION
try:
    myfile = open("lo.txt","r")
    print("Success in reading")
except:
    print("File not exist")
print("Task Done")