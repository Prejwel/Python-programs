
def main():

#Create a file and Write to that file
#------------------------------------
    # file = open("lco.txt","w+")
    # file.write("Hello world , I am writing to a file")
    # file.close()
#------------------------------------------------------

#Open a file and Read it
    # file = open("lco.txt",'r')
    # if file.mode == 'r':
    #     contents = file.read()
    #     print(contents)
    #     file.close()

#--------------------------------
#To Append to file and then to read it
    file = open("abc.txt",'a+')
    file.write(" Python")


files = open("abc.txt",'r')
if files.mode == 'r':
    for r in range(5):
        print(r)
        contents = files.read()
        print("\n",contents)
        files.close()
#--------------------------------------------------
# Main Method
if __name__ == '__main__':
    main()