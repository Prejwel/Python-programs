upperRange = int(input("Enter the upper Range"))
lowerRange = int(input("Enter the lower Range"))
#number = int(input("Enter a Number with in the range"))

for number in range(lowerRange,upperRange):
    if number > 1:
        for i in range(2,number):
            if number%i==0:
                print("%d Prime Number"%number)
                break
        else:
            print("%d Not a prime number"%number)

#If the number is between the upper and lower range and
# if the number is greater than one and
# if its properly divisible by any number (reminder=0).
# Then the number is prime number.