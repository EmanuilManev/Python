flour = input("Въведете цена на брашното: ")
n_flour = input("Въведете необходимо к-во брашно: ")
n_sugar = input("Въведете необходимо к-во захар: ")
n_eggs = input("Въведете необходим бр кори за яйца: ")
n_yeast = input("Въведете необходим бр пакети мая: ")
sugar = round(float(flour) * 0.75, 2)
eggs = round(float(flour) * 1.1, 2)
yeast = round(float(sugar) * 0.2, 2)
total = round(float(flour) * float(n_flour) + eggs * float(n_eggs) + sugar * float(n_sugar) + yeast * float(n_yeast), 2)
print(total)