import math
kozunak = int(input())
index = 1
l_sugar = 0
l_flour = 0
m_sugar = 0
m_flour = 0

for index in range(kozunak):
    sugar = int(input())
    flour = int(input())
    l_sugar += sugar
    l_flour += flour
    if m_sugar < sugar:
        m_sugar = sugar
    if m_flour < flour:
        m_flour = flour
print("Sugar: " + str(math.ceil(l_sugar/950)))
print("Flour: " + str(math.ceil(l_flour/750)))
print("Max used flour is " + str(m_flour) + " grams, max used sugar is " + str(m_sugar) + " grams.")




