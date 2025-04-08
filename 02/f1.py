#!/usr/bin/env python

import pygame
import math
import copy

FRAMES_PER_SECOND = 60
BG_COLOR = (255, 255, 0)
FG_COLOR = (0, 0, 255)
WINDOW_SIZE = (600, 600)
CENTER = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)
POLY_SIDES = 19
POLY_ANGLE = - math.pi / 2 # in radians
POLY_RADIUS = 150

def get_poly_points(sides, angle, center, radius):
	points = []
	x, y = center[0], center[1]
	for i in range(sides):
		point_x = x + radius * math.cos(angle + 2 * math.pi * i / sides)
		point_y = y + radius * math.sin(angle + 2 * math.pi * i / sides)
		points.append([int(point_x), int(point_y)])
	return points

def scale_poly(points, center, scale_x, scale_y):
	cx, cy = center[0], center[1]
	new_points = []
	for x, y in points:
		dx = x - cx
		dy = y - cy
		new_dx = dx * scale_x
		new_dy = dy * scale_y
		new_x = cx + new_dx
		new_y = cy + new_dy
		new_points.append((int(new_x), int(new_y)))
	return new_points

def rotate_poly(points, center, angle):
	cx, cy = center[0], center[1]
	new_points = []
	sin_angle = math.sin(angle)
	cos_angle = math.cos(angle)
	for x, y in points:
		dx = x - cx
		dy = y - cy
		new_dx = dx * cos_angle - dy * sin_angle
		new_dy = dx * sin_angle + dy * cos_angle
		new_x = cx + new_dx
		new_y = cy + new_dy
		new_points.append((int(new_x), int(new_y)))
	return new_points

def skew_poly(points, center, shear_x, shear_y):
	cx, cy = center[0], center[1]
	new_points = []
	for x, y in points:
		dx = x - cx
		dy = y - cy
		new_dx = dx + shear_x * dy
		new_dy = dy + shear_y * dx
		new_x = cx + new_dx
		new_y = cy + new_dy
		new_points.append((int(new_x), int(new_y)))
	return new_points

def move_poly(points, offset_x, offset_y):
	new_points = []
	for x, y in points:
		new_x = x + offset_x
		new_y = y + offset_y
		new_points.append((int(new_x), int(new_y)))
	return new_points

INITIAL_POINTS = get_poly_points(POLY_SIDES, POLY_ANGLE, CENTER, POLY_RADIUS)
current_points = copy.deepcopy(INITIAL_POINTS)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_0:
				current_points = copy.deepcopy(INITIAL_POINTS)
			elif event.key == pygame.K_1:
				current_points = scale_poly(INITIAL_POINTS, CENTER, 0.5, 0.5)
			elif event.key == pygame.K_2:
				current_points = rotate_poly(INITIAL_POINTS, CENTER, math.pi / 4)
			elif event.key == pygame.K_3:
				current_points = scale_poly(INITIAL_POINTS, CENTER, 0.5, -1)
			elif event.key == pygame.K_4:
				current_points = skew_poly(INITIAL_POINTS, CENTER, 0.15, 0)
			elif event.key == pygame.K_5:
				tmp_points = scale_poly(INITIAL_POINTS, CENTER, 1, 0.5)
				current_points = move_poly(tmp_points, 0, -200)
			elif event.key == pygame.K_6:
				tmp_points = skew_poly(INITIAL_POINTS, CENTER, 0.15, 0)
				current_points = rotate_poly(tmp_points, CENTER, math.pi / 2)
			elif event.key == pygame.K_7:
				current_points = scale_poly(INITIAL_POINTS, CENTER, -0.5, -1)
			elif event.key == pygame.K_8:
				tmp_points = scale_poly(INITIAL_POINTS, CENTER, 1, 0.5)
				tmp_points = rotate_poly(tmp_points, CENTER, math.pi / 6)
				current_points = move_poly(tmp_points, -100, 150)
			elif event.key == pygame.K_9:
				tmp_points = scale_poly(INITIAL_POINTS, CENTER, -1, -1)
				tmp_points = skew_poly(tmp_points, CENTER, 0, 0.15)
				current_points = move_poly(tmp_points, 100, 0)
	screen.fill(BG_COLOR)
	pygame.draw.polygon(screen, FG_COLOR, current_points)
	pygame.display.flip()
	clock.tick(FRAMES_PER_SECOND)

pygame.quit()
