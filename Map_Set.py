# Map - using map , we can map a method with set

superhero = {1,2,3,4,3.0}
print(superhero) # here it wont take 3.0 (3/3.0 one and the same and set cant have duplicate value)
print(len(superhero))
def getSquare(num):
    return num*num
result = map(getSquare,superhero)
finalResult = set(result)
print(finalResult)