import assig_Calculator
num1=int(input("Enter the 1st Value"))
num2=int(input("Enter the 2nd Value"))

print("Press 1 for Addition\n Press 2 for Subtraction\n Press 3 for Multiplication\n Press 4 for Division")
value=int(input("Enter the Number for calculation"))

if value == 1:
    print(assig_Calculator.add(num1,num2))
elif value == 2:
    print(assig_Calculator.sub(num1,num2))
elif value == 3:
    print(assig_Calculator.multiply(num1,num2))
elif value == 4:
    print(assig_Calculator.divide(num1,num2))
else:
    print("Please enter a value from 1 to 4")


#created a file assig_Calculator
#created functions in the file
#imported that file and used that file functions for calculation here