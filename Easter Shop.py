available = int(input())
order = str("")
qtty = int()
sold = 0
while order != "Close":
    order = input()
    if order == "Fill":
        qtty = int(input())
        available += qtty
    elif order == "Buy":
        qtty = int(input())
        if (available - qtty) >= 0:
            available -= qtty
            sold += qtty
        else:
            print("Not enough eggs in store!")
            print("You can buy only " + str(available) + ".")
            break
else:
    if order == "Close":
        print("Store is closed!")
        print(str(sold) + " eggs sold.")
