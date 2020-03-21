guests = int(input("Брoй гости - цяло число в интервала [1...99]"))
voucher = float(input("Цена на куверт за един човек - реално число в интервала [0.00 ... 99.00]"))
budget = float(input("Бюджетът на Деси - реално число в интервала [0.00 ... 9999.00]"))

if guests <= 15 and guests >= 10:
    total = round(guests * voucher * 0.85 + budget * 0.1, 2)
    if budget >= total:
        print("It's party time! " + '{:.2f}'.format(budget - total) + " leva left.")
    else:
        print("No party! " + '{:.2f}'.format(total - budget) + " leva needed.")
elif guests <= 10:
    total = round(guests * voucher + budget * 0.1, 2)
    if budget >= total:
        print("It's party time! " + '{:.2f}'.format(budget - total) + " leva left.")
    else:
        print("No party! " + '{:.2f}'.format(total - budget) + " leva needed.")
if guests <= 20 and guests > 15:
    total = round(guests * voucher * 0.8 + budget * 0.1, 2)
    if budget >= total:
        print("It's party time! " + '{:.2f}'.format(budget - total) + " leva left.")
    else:
        print("No party! " + '{:.2f}'.format(total - budget) + " leva needed.")
if guests > 20:
    total = round(guests * voucher * 0.75 + budget * 0.1, 2)
    if budget >= total:
        print("It's party time! " + '{:.2f}'.format(budget - total) + " leva left.")
    else:
        print("No party! " + '{:.2f}'.format(total - budget) + " leva needed.")