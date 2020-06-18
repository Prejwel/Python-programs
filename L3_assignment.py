#we have a product and its price is 100.
#user wil pass 2 numbers.
#final product value will be the result after substracting the 2 values from 100.

def final_value(*num):
    product_value=100
    for i in num:
        product_value=product_value-i
        #print(product_value)
    return product_value
a=int(input("Enter the 1st Value"))
b=int(input("Enter the 2nd Value"))
print(final_value(a,b))

