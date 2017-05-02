import numpy as np
import cv2
import socket
import pygame
from pygame.locals import *
import serial
import sys

e1 = cv2.getTickCount()
image_array = np.zeros((1, 38400))
label_array = np.zeros((1, 4), 'float')

server_socket = socket.socket()
server_socket.bind(('192.168.1.105', 8000))
server_socket.listen(0)
connection, client_address = server_socket.accept()
connection = connection.makefile('rb')

print("Server Up")
serial_port = serial.Serial('COM5', 9600, timeout=1)

def write(int):
    return serial_port.write(chr(int))

pygame.init()
pygame.display.set_mode((100,100))

saved_frame = 0
total_frame = 0

print("Connection from: ", client_address)
print("Streaming...")
print("Press 'q' to exit")

k = np.zeros((4, 4), 'float')
for i in range(4):
    k[i, i] = 1
    temp_label = np.zeros((1, 4), 'float')

stream_bytes = ' '
while True:
    stream_bytes += connection.read(1024)
    first = stream_bytes.find('\xff\xd8')
    last = stream_bytes.find('\xff\xd9')
    if first != -1 and last != -1:
        jpg = stream_bytes[first:last + 2]
        stream_bytes = stream_bytes[last + 2:]
        #image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.CV_LOAD_IMAGE_GRAYSCALE)
        image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
        roi = image[120:240, :]
        cv2.imshow('image', image)
        temp_array = roi.reshape(1, 38400).astype(np.float32)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            key_input = pygame.key.get_pressed()

            if key_input[pygame.K_UP] and key_input[pygame.K_RIGHT]:
                print("Forward Right")
                saved_frame +=1
                write(5)
                image_array = np.vstack((image_array, temp_array))
                label_array = np.vstack((label_array, k[1]))
            elif key_input[pygame.K_UP] and key_input[pygame.K_LEFT]:
                saved_frame += 1
                write(6)
                image_array = np.vstack((image_array, temp_array))
                label_array = np.vstack((label_array, k[0]))
            elif key_input[pygame.K_DOWN] and key_input[pygame.K_RIGHT]:
                saved_frame += 1
                write(7)
            elif key_input[pygame.K_DOWN] and key_input[pygame.K_LEFT]:
                saved_frame += 1
                write(8)
            elif key_input[pygame.K_UP]:
                saved_frame += 1
                write(1)
                image_array = np.vstack((image_array, temp_array))
                label_array = np.vstack((label_array, k[2]))
            elif key_input[pygame.K_DOWN]:
                saved_frame += 1
                write(2)
                image_array = np.vstack((image_array, temp_array))
                label_array = np.vstack((label_array, k[3]))
            elif key_input[pygame.K_RIGHT]:
                saved_frame += 1
                write(3)
                image_array = np.vstack((image_array, temp_array))
                label_array = np.vstack((label_array, k[1]))
            elif key_input[pygame.K_LEFT]:
                saved_frame += 1
                write(4)
                image_array = np.vstack((image_array, temp_array))
                label_array = np.vstack((label_array, k[0]))
            elif key_input[pygame.K_x] or key_input[pygame.K_q] or key_input[pygame.K_ESCAPE]:
                print("Exit")
                write(0)
                sys.exit()
        elif event.type == pygame.KEYUP:
            write(0)


    train = image_array[1:, :]
    train_labels = label_array[1:, :]

    np.savez('test_dataset.npz', train=train, train_labels=train_labels)
    e2 = cv2.getTickCount()
    # calculate streaming duration
    #time0 = (e2 - e1) / cv2.getTickFrequency()
    #print('Streaming duration:', time0)
"""finally:
    connection.close()
    server_socket.close()"""