import socket
import cv2
import numpy as np

server_socket = socket.socket()
#socket.AF_INET, socket.SOCK_STREAM
server_socket.bind(('192.168.1.104', 8000))
server_socket.listen(0)

connection = server_socket.accept()[0].makefile('rb')

saved_frame = 0
total_frame = 0

# collect images for training
print 'Start collecting images...'
e1 = cv2.getTickCount()
image_array = np.zeros((1, 38400))
label_array = np.zeros((1, 4), 'float')

try:
	stream_bytes = ''
	frame = 1
	while True:
		#read_data = connection.read(1024)
		stream_bytes += connection.read(1024)
		first = stream_bytes.find('\xff\xd8')
		last = stream_bytes.find('\xff\xd9')
		if first != -1 and last != -1:
			jpg = stream_bytes[first:last + 2]
			stream_bytes = stream_bytes[last + 2:]
			image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
			# select lower half of the image
			#roi = image[120:240, :]
			# save streamed images
			cv2.imwrite('training_images/frame{:>05}.jpg'.format(frame), image)
			#read_1 = cv2.imread(read_data)
			#cv2.imshow('roi_image', roi)
			cv2.namedWindow('image', cv2.WINDOW_NORMAL)
			cv2.imshow('image', image)
			# reshape the roi image into one row array
			#temp_array = roi.reshape(1, 38400).astype(np.float32)
			#train = image_array[1:, :]
			frame += 1
			total_frame += 1
finally:
	connection.close()
	server_socket.close()