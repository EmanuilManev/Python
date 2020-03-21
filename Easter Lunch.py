kozunaks = int(input("Бр. козунаци: "))
eggs = int(input("Бр. кори за яйца: "))
cookies = int(input("Кг. курабии: "))

total = kozunaks * 3.2 + eggs * (4.35 + 12*0.15) + cookies * 5.4
print('{:.2f}'.format(total))