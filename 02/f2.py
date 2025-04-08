#!/usr/bin/env python

import pygame

FRAMES_PER_SECOND = 60
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
WINDOW_SIZE = (600, 600)
CENTER = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.fill(WHITE)
	pygame.draw.rect(screen, BLUE, (200, 250, 200, 100))
	pygame.draw.polygon(screen, BLUE, [(250, 150), (350, 150), (300, 250)])
	pygame.draw.polygon(screen, BLUE, [(300, 350), (350, 450), (250, 450)])
	pygame.display.flip()
	clock.tick(FRAMES_PER_SECOND)

pygame.quit()
