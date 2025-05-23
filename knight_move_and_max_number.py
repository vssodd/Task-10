x = float(input('Введите местоположение коня X: '))
y = float(input('Введите местоположение коня Y: '))
deskX = float(input('Введите местоположение точки на доске X: '))
deskY = float(input('Введите местоположение точки на доске Y: '))

# Convert coordinates to board cells (scaled to 10x10)
xSquare = int(x * 10)
ySquare = int(y * 10)
bxSquare = int(deskX * 10)
bySquare = int(deskY * 10)

print('Конь в клетке', xSquare, ',', ySquare, 'Точка в клетке', bxSquare, ',', bySquare)

# Calculate the absolute difference
diff_x = abs(x - deskX)
diff_y = abs(y - deskY)

# Check knight movement condition
if abs(diff_x * diff_y) == 2:
    print('Да, конь может ходить в эту точку.')
else:
    print('Нет, конь не может ходить в эту точку.')

#  Maximum Finder Without Using max()
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Calculate difference and derive the larger number
diff = num1 - num2
result = num1 - diff * (diff < 0)

print('Наибольшее число:', round(result))
