# Map - using map , we can map a method with set

superhero = {1,2,3,4}
print(superhero) # here it wont print 3.0 (3/3.0 one and the same bcz its a duplicate value)

def getSquare(num):
    return num*num
result = map(getSquare,superhero)
finalResult = set(result)
print(finalResult)