result = str("")
t_tournaments = int(input())
start_points = int(input())
t_points = 0
win = 0
tournaments = 0

for index in range(t_tournaments):
    result = input()
    tournaments += 1
    if result == "W":
        t_points += 2000
        win += 1
    elif result == "F":
        t_points += 1200
    elif result == "SF":
        t_points += 720
print("Final points: " + str(t_points + start_points))
print("Average points: " + str(t_points // tournaments))
print(str('{:.2f}'.format(win / tournaments * 100) + "%"))