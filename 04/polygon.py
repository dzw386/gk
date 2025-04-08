#!/usr/bin/env python

import math

def get_poly_points(sides, angle, center, radius):
	points = []
	x, y = center[0], center[1]
	for i in range(sides):
		point_x = x + radius * math.cos(angle + 2 * math.pi * i / sides)
		point_y = y + radius * math.sin(angle + 2 * math.pi * i / sides)
		points.append([point_x, point_y])
	return points

points = get_poly_points(19, 0, (0, 0), 1)

print('<polygon points="')
for p in points:
	print('\t' + str(p[0]) + ', ' + str(p[1]))
print('" />')

for p in points:
	print('<line x1="0" y1="0" x2="' + str(p[0]) + '" y2="' + str(p[1]) + '" />')
