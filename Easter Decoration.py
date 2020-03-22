customers = 0
products = str("")
total = 0
index = 1
num = 0
average = 0

customers = int(input())
for index in range(customers):
    while products != "Finish":
        products = input()
        if products == "basket":
            total = total + 1.5
            num += 1
        elif products == "wreath":
            total = total + 3.8
            num += 1
        elif products == "chocolate bunny":
            total = total + 7
            num += 1
    if num % 2 == 0:
        total = round(total * 0.8, 2)
    print("You purchased " + str(num) + " items for " + str('{:.2f}'.format(total)) + " leva.")
    products = str("")
    average += total
    total = 0
    num = 0
print("Average bill per client is: " + str('{:.2f}'.format(average / customers)) + " leva.")
