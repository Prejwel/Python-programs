row = int(input("Enter the number of Rows"))
column = int(input("Enter the number of Columns"))

matrix=[]         # Main empty matrix to which we need to add elements
print(" Enter the Row Values")

# TODO taking Input to matrix
for i in range(row): #starting with 1st row
    a=[]
    for j in range(column):
        a.append(int(input())) #prompting to enter the values to the columns of 1st row
    matrix.append(a)

# TODO print Matrix
for i in range(row):
    for j in range(column):
        print(matrix[i][j],end=" ")
    print()