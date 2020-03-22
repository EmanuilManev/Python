batki = int(input())
workout = str("")
back = 0
chest = 0
legs = 0
abss = 0
ps = 0
pb = 0

for index in range(batki):
    workout = input()
    if workout == "Back":
        back += 1
    elif workout == "Chest":
        chest += 1
    elif workout == "Legs":
        legs += 1
    elif workout == "Abs":
        abss += 1
    elif workout == "Protein bar":
        pb += 1
    elif workout == "Protein shake":
        ps += 1

print(str(back) + " - back")
print(str(chest) + " - chest")
print(str(legs) + " - legs")
print(str(abss) + " - abs")
print(str(ps) + " - protein shake")
print(str(pb) + " - protein bar")
print(str('{:.2f}'.format((back + chest + legs + abss) / batki * 100) + "% - work out"))
print(str('{:.2f}'.format((pb + ps) / batki * 100) + "% - protein"))
