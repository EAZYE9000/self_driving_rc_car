import pygame
from pygame.locals import *

pygame.init()

keys = pygame.key.get_pressed()
if keys[K_LEFT]:
	print("LEFT")
elif keys[K_RIGHT]:
	print("RIGHT")