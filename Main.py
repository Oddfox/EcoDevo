#! /usr/bin/env python

import pygame    


running = 1
screenWidth = 800
screenHeight = 600    
bgColor = 0, 0, 0
rectColor = 255, 0, 0

screen = pygame.display.set_mode((screenWidth, screenHeight))

while running:
    
    screen.fill(bgColor)
    pygame.draw.rect((screen), (rectColor), (0, 0, 25, 25))
    
    
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
        
    pygame.display.flip()