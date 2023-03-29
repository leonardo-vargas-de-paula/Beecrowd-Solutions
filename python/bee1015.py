x1, y1 = list(map(float, input().split()))
x2, y2 = list(map(float, input().split()))
dAB = ((x1 - x2) ** 2 + (y1 - y2)**2) ** (1/2)
print('%0.4f'%dAB)