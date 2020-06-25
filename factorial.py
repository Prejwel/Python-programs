number=int(input("Enter a number "))
factorial=1
if number>1:
    for i in range(1,number+1):
        factorial=factorial*i     # 1*2*3*4* ....
    print("factorial=",factorial)
elif number == 1:
    print("Factorial of 1 is 1")
elif number==0:
    print("Factorial of 0 is 1")


#Reverse order
# num=int(input("enter a number"))
# result=1
# if num>0:
#     for i in range(num,0,-1):
#         result=result*i
#     print("Factorial",result)
# elif num==0:
#     print("Factorial of 0 is 1")