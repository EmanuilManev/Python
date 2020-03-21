player1 = int(input())
player2 = int(input())

battle = str("")
while player1 > 0 and player2 > 0 and battle != "End of battle":
    battle = input()
    if battle == "one":
        player2 = player2 - 1
    elif battle == "two":
        player1 = player1 - 1

if player1 > player2 and battle != "End of battle":
   print("Player two is out of eggs. Player one has " + str(player1) + " eggs left.")
elif player2 > player1 and battle != "End of battle":
   print("Player one is out of eggs. Player two has " + str(player2) + " eggs left.")
else:
    print("Player one has " + str(player1) + " eggs left. Player two has " + str(player2) + " eggs left.")