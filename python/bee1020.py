x = int(input())
a = x//365
m = (x % 365)//30
d = (x % 365)%30
print(f"{a} ano(s)\n{m} mes(es)\n{d} dia(s)")