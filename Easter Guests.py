guests = int(input("Да се въведе бр на гостите в интервала 0 до 200000: "))
budget = int(input("Да се въведе бюджета ла Любо в интервала 0 до 200000: "))

if guests >= 0 and guests <= 200000 and budget >= 0 and budget <= 200000:
    eggs = guests * 2
    if guests % 3 != 0:
        easter_bread = guests//3 + 1
        total = round(eggs * 0.45 + easter_bread * 4, 2)
        if total > budget:
            print("Lyubo doesn't have enough money")
            print("He needs " + str('{:.2f}'.format(total - budget)) + " more.")
        else:
            print("Lyubo bought " + str(easter_bread) + " Easter bread and " + str(eggs) + " eggs")
            print("He has " + '{:.2f}'.format(budget - total) + " lv. left.")
    else:
        easter_bread = guests / 3
        total = round(eggs * 0.45 + easter_bread * 4, 2)
        if total > budget:
            print("Lyubo doesn't have enough money")
            print("He needs " + str('{:.2f}'.format(total - budget)) + " more.")
        else:
            print("Lyubo bought " + str(easter_bread) + " Easter bread and " + str(eggs) + " eggs")
            print("He has " + '{:.2f}'.format(budget - total) + " lv. left.")
