countries = input()
dates = input()
nights = int(input())

l_countries = ["France", "Italy", "Germany"]
l_dates = ["21-23", "24-27", "28-31"]
l_price = [
    [30, 35, 40],
    [28, 32, 39],
    [32, 37, 43]
    ]
total = nights * l_price[l_countries.index(countries)][l_dates.index(dates)]
print("Easter trip to " + countries + " : " + str('{:.2f}'.format(total)) + " leva.")