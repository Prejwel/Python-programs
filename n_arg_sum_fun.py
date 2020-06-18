# program to add all the numbers given as argument using a function
#total=0
def addme(*num):
    total=0
    for i in num:
        total=total+i
        print(i)
    return total

print(addme(1,2,3,4))
