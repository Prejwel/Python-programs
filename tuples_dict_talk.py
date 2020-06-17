marvel_Heros=("Spiderman","Ironman","Thor")
dc_Heros=("Batman","Superman","Flash","Aquaman")

#Tuple
heros=marvel_Heros+dc_Heros
print(heros)

#Dictionary
batsman={
    "Sachin":100,
    "Dravid":90,
    "Saurav":95
}

bowlers={
    "Zaheer":95,
    "Bumbrah":90,
    "Shami":80
}

print("Length of Batsman Dictionary=",len(batsman))
# batsman.clear()
# print("Batsman Dict",batsman)

 #update
batsman.update(bowlers)
print("Updated Dict",batsman)

myTags=("Name", "Address", "PhoneNo")
myOne=dict.fromkeys(myTags)
print("My Dictionary is  %s"%str(myOne))

#here contents of tuple is converted to dictionary and is printed out

# #Tuple
# -------
# update
#
# Dictionary
# -----------
# length
# clear
# update
# dict.fromkeys()