 # using yield instead of return to make the object iteratable

import random

heros = ["Batman","Hulk","Thor"]

def magic():
    for i in range(6):
        yield random.randint(0,20)  # majking it iteratable using yield
for number in magic():
    print(number)