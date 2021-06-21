h = int(input('근무시간'))
p = int(input('시간당 임금'))

if h > 40:
    over = h - 40
    total = p * 40 + over * p * 1.5
else:
    total = h * p

print(f'total{total}')
