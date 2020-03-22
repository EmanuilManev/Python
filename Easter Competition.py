kozunak = int(input())
index = 1
vhod = str("")
score = 0
m_score = 0
top_chef = str("")
for index in range(kozunak):
    chef = input()
    while vhod != "Stop":
        vhod = input()
        if vhod != "Stop":
            score += int(vhod)
    print(str(chef) + " has " + str(score) + " points.")
    if score > m_score:
        m_score = score
        top_chef = chef
        print(str(chef) + " is the new number 1!")
    vhod = str("")
    score = 0
print(str(top_chef) + " won competition with " + str(m_score) + " points!")
