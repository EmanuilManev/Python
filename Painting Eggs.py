Size = input()
Colour = input()
Number = int(input())

l_size = ["Large", "Medium", "Small"]
l_colour = ["Red", "Green", "Yellow"]
l_price = [
    [16, 12, 9],
    [13, 9, 7],
    [9, 8, 5]
]

total = Number * l_price[l_size.index(Size)][l_colour.index(Colour)] * 0.65
print(str('{:.2f}'.format(total)) + " leva.")