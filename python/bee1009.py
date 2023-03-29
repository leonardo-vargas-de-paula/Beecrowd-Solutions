nome = input()
sal = float(input())
vend = float(input())
bonus = float(vend * (15/100))
total = sal + bonus
print("TOTAL = R$ %0.2f" %total)