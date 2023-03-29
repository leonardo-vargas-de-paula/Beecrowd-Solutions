money = int(input())
n100 = money // 100
x = money % 100
n50 = x // 50
y = x % 50
n20 = y // 20
z = y % 20
n10 = z // 10
v = z % 10
n5 = v // 5
m = v % 5
n2 = m // 2
l = m % 2
n1 = l // 1
print(money)
print(f'{n100} nota(s) de R$ 100,00')
print(f'{n50} nota(s) de R$ 50,00')
print(f'{n20} nota(s) de R$ 20,00')
print(f'{n10} nota(s) de R$ 10,00')
print(f'{n5} nota(s) de R$ 5,00')
print(f'{n2} nota(s) de R$ 2,00')
print(f'{n1} nota(s) de R$ 1,00')