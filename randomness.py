import random
my_list=[3,5.0,"Prejwel",100]
print(my_list)
print("Choice=",random.choice(my_list))

print("RandRange(Start,Stop,Step)=",random.randrange(0,100,3))

print("Random_Random ",random.random())

random.seed(10)
print("Random.Random with SEED = ", random.random())

random.shuffle(my_list)
print("MyList got shuffled")
print("Random Shuffled value of myList =",my_list)