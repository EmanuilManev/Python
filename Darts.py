player = input()
points = 0
t_points = 301
win = 0
lost = 0

while t_points > 0:
    bonus = input()
    if bonus == "Retire":
        print(player + " retired after " + str(lost) + " unsuccessful shots.")
        break
    points = int(input())
    if bonus == "Double":
        points = 2 * points
    elif bonus == "Triple":
        points = 3 * points
    if t_points - points > 0:
        t_points -= points
        win += 1
    elif t_points == points:
        t_points -= points
        win += 1
        print(player + " won the leg with " + str(win) + " shots.")
    else:
        lost += 1

