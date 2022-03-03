n = int( input('n = '))
k = int( input('k = '))
quotient, remainder = divmod( n, k ) # частное и остаток
res = []
for i in range(remainder):
    res.append(quotient+1)
for i in range(k-remainder):
    res.append(quotient)
print( f'Разбиение массива длиной {n} на {k} подмассивов с длинами:' )
print(res)