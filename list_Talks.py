marvel_heros=["Spiderman","Ironman","Thor"]
dc_heros=["Batman","Flash","Aquaman"]

marvel_heros[2]="Hulk"
print(marvel_heros)

dc_heros.append("Superman")
print(dc_heros)

dc_heros.insert(0,"Green Arrow")
print(dc_heros)

dc_heros.remove("Flash")
print(dc_heros)

dc_heros.reverse()
print(dc_heros)

print(dc_heros.count("Batman"))

#Assignment - to combine  the lists
print(marvel_heros+dc_heros)
