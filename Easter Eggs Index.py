eggs = int(input())
index = 1
red = 0
orange = 0
blue = 0
green = 0
max_eggs = [red, orange, blue, green]
colours = ["red", "orange", "blue", "green"]
for index in range(eggs):
    colour = input()
    max_eggs[colours.index(colour)] += 1

print("Red eggs: " + str(red))
print("Orange eggs: " + str(orange))
print("Blue eggs: " + str(blue))
print("Green eggs: " + str(green))
print("Max eggs: " + str(max(max_eggs)) + " -> " + colours[max_eggs.index(max(max_eggs))])
