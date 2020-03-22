win = 0
lost = 0
games = 0
t_games = 0
home_score = 0
away_score = 0
score = 0
tournament = str("")


while tournament != "End of tournaments":
    tournament = input()
    if tournament == "End of tournaments":
        break
    games = int(input())
    index = 1
    tour_games = 0
    for index in range(games):
        home_score = int(input())
        away_score= int(input())
        t_games += 1
        tour_games += 1
        score = abs(home_score - away_score)
        if home_score > away_score:
            win += 1
            print("Game " + str(tour_games) + " of tournament " + tournament + ": win with " + str(score) + " points.")
        else:
            lost += 1
            print("Game " + str(tour_games) + " of tournament " + tournament + ": lost with " + str(score) + " points.")
print(str('{:.2f}'.format(win / t_games * 100)) + "% matches win")
print(str('{:.2f}'.format(lost / t_games * 100)) + "% matches lost")