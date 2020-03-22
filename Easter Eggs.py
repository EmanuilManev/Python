
eggs = int(input())
index = 1
red = 0
orange = 0
blue = 0
green = 0

for index in range(eggs):
    colour = input()
    if colour == "red":
        red += 1
    elif colour == "orange":
        orange += 1
    elif colour == "blue":
        blue += 1
    elif colour == "green":
        green += 1
max_eggs = [red, orange, blue, green]
colours = ["red", "orange", "blue", "green"]
print("Red eggs: " + str(red))
print("Orange eggs: " + str(orange))
print("Blue eggs: " + str(blue))
print("Green eggs: " + str(green))
print("Max eggs: " + str(max(max_eggs)) + " -> " + colours[max_eggs.index(max(max_eggs))])
