xseg = int(input())
xh = xseg // 3600
xm = ((xseg - xh) // 60) % 60
xs = (xseg- xh * 3600 - xm * 60)
print(f'{xh}:{xm}:{xs}')