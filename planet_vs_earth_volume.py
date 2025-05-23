import math

R = float(input('Enter the radius of the planet: '))
volume_earth = 10.8321 * 10 ** 11
volume_planet = (4/3) * math.pi * (R ** 3)

if volume_planet > volume_earth:
    compare = round(volume_planet / volume_earth, 3)
    print('The discovered planet is smaller than Earth by', compare, 'times')
elif volume_planet < volume_earth:
    compare = round(volume_earth / volume_planet, 3)
    print('The discovered planet is larger than Earth by', compare, 'times')
else:
    print('The discovered planet and Earth have the same volume')
