import random

print("Range value =",random.choice(range(10)))
print("List value=",random.choice([1,2,3,4,5]))
print("String Value=",random.choice("Prejwel"))

#random.randrange(start,stop,step)
print("RandRangerValue=",random.randrange(1,100,5))

print("Random Value without seed=",random.random())

random.seed(10)
print("random Value with SEED=",random.random())

list_numbers=[2,4,6,8]
random.shuffle(list_numbers)
print(list_numbers)

#-----------------
# random.choice
#random.randrange
#random.random
#random.shuffle
#random.seed
#------------------