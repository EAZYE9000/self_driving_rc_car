import pygame
from pygame.locals import *
import serial
import sys

serial_port = serial.Serial('COM5', 9600, timeout=1)

def write(int):
	return serial_port.write(chr(int))

pygame.init()
pygame.display.set_mode((100,100))

saved_frame = 0
total_frame = 0
while True:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			key_input = pygame.key.get_pressed()

			if key_input[pygame.K_UP] and key_input[pygame.K_RIGHT]:
				print("Forward Right")
				saved_frame +=1
				write(5)
			elif key_input[pygame.K_UP] and key_input[pygame.K_LEFT]:
				saved_frame += 1
				write(6)
			elif key_input[pygame.K_DOWN] and key_input[pygame.K_RIGHT]:
				saved_frame += 1
				write(7)
			elif key_input[pygame.K_DOWN] and key_input[pygame.K_LEFT]:
				saved_frame += 1
				write(8)
			elif key_input[pygame.K_UP]:
				saved_frame += 1
				write(1)
			elif key_input[pygame.K_DOWN]:
				saved_frame += 1
				write(2)
			elif key_input[pygame.K_RIGHT]:
				saved_frame += 1
				write(3)
			elif key_input[pygame.K_LEFT]:
				saved_frame += 1
				write(4)
			elif key_input[pygame.K_x] or key_input[pygame.K_q] or key_input[pygame.K_ESCAPE]:
				print("Exit")
				write(0)
				sys.exit()
		elif event.type == pygame.KEYUP:
			write(0)
""" its all wonderful and great, you can press 2 keys at once... until you want to go back to one. If you're going forward + right, then you want to stop turining, Uh-ohs! Buckeroo you're fucked. You have to re-press the keys, no fucking clue how to fix that now, been up the road and round the bend trying to. For now I will take a break."""