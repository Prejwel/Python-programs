number=int(input("Enter a number greater than 1"))
if number>1:
    for i in range(2,number):
        print(" i = ",i)
        if (number%i==0):
            print("Prime Number")
            print("How many times=",number//i)
            break
    else:
        print("%d is not a prime number"%(number))
