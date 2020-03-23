player_one = input()
player_two = input()
card_one = 0
card_two = 0
drawn = 0
points_one = 0
points_two = 0

while drawn <= 34:
    print(drawn)
    card_one = input()
    if card_one == "End of game":
        print(player_one + " has " + str(points_one) + " points")
        print(player_two + " has " + str(points_two) + " points")
        break
    drawn += 1
    card_two = input()
    drawn += 1
    if int(card_one) > int(card_two):
        points_one += abs(int(card_one) - int(card_two))
    elif int(card_one) < int(card_two):
        points_two += abs(int(card_one) - int(card_two))
    elif int(card_one) == int(card_two):
        print("Number wars!")
        card_one = input()
        drawn += 1
        card_two = input()
        drawn += 1
        if int(card_one) > int(card_two):
            print(player_one + " is winner with " + str(points_one) + " points")
        else:
            print(player_two + " is winner with " + str(points_two) + " points")
        print()
        break
