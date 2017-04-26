import serial
import sys, termios, tty, os, time

serial_port = serial.Serial('/dev/cu.usbmodem1A1341', 9600, timeout=1)

#while True:
#	serial_port.write(chr(0))

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
button_delay = 0.2

def stop():
	serial_port.write(chr(0))

orig_settings = termios.tcgetattr(sys.stdin)

#tty.setraw(sys.stdin)
x = 0

while x != chr(27): #ESC Key
	
	char = getch()
	#x=sys.stdin.read(1)[0]
	#print("You pressed", x)
	#print(x)

	"""if char != "w" and "a" and "s" and "d":
		stop()
		print("stop")"""
	if char == "s":
		serial_port.write(chr(2))
		print("BACKWARD")
	elif char == "w":
		serial_port.write(chr(1))
		print("FORWARD")
	elif char == "a":
		serial_port.write(chr(4))
		print("LEFT")
	elif char == "d":
		serial_port.write(chr(3))
		print("RIGHT")
	elif char == "w" + char == "d":
		serial_port.write(chr(5))
		print("FORWARD RIGHT")
	elif char == "w" + char == "a":
		serial_port.write(chr(6))
		print("FORWARD LEFT")
	elif char == "s" + char == "d":
		serial_port.write(chr(7))
		print("BACKWARD RIGHT")
	elif char == "s" + char == "a":
		serial_port.write(chr(8))
		print("BACKWARD LEFT")
	elif char == "q":
		serial_port.write(chr(0))
		stop()
		break
	else:
		stop()
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings) # not able to serial_port.write(chr(3)) with the keystroke detection for some reason. The main problem with the other solution was when you press W the car KEEPS going forward even after release and only until another key is pressed. Trying to combat this with keystroke detection, maybe something like if key == nil: write(chr(0)).r3w