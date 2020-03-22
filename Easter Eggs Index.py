eggs = int(input())
index = 1

max_eggs = [0, 0, 0, 0]
colours = ["red", "orange", "blue", "green"]
for index in range(eggs):
    colour = input()
    max_eggs[colours.index(colour)] += 1

print("Red eggs: " + str(max_eggs[1]))
print("Orange eggs: " + str(max_eggs[2]))
print("Blue eggs: " + str(max_eggs[3]))
print("Green eggs: " + str(max_eggs[4]))
print("Max eggs: " + str(max(max_eggs)) + " -> " + colours[max_eggs.index(max(max_eggs))])
