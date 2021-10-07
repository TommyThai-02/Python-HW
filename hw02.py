#Author: Tommy Thai
#Filename: hw02.py
#Assignment#: hw02

import math
r = input('Enter a radius of a circle:')
circlearea =(math.pi*float(r)**2)
circlecircumference = (2*math.pi*float(r))
print('Area of the circle:  ' + format(circlearea, '.3f'), 'Circle circumference:' + format(circlecircumference, '.3f'), sep ='\n')

