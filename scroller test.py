import math 
import pygame as py 

py.init() 

clock = py.time.Clock() 

FrameHeight = 900
FrameWidth = 1024

# PYGAME FRAME WINDOW 
py.display.set_caption("Endless Scrolling in pygame") 
screen = py.display.set_mode((FrameWidth, 
							FrameHeight)) 

# IMAGE 
bg = py.image.load("Assets/Blank-Background.png").convert() 

# DEFINING MAIN VARIABLES IN SCROLLING 
scroll = 0

# CHANGE THE BELOW 1 TO UPPER NUMBER IF 
# YOU GET BUFFERING OF THE IMAGE 
# HERE 1 IS THE CONSTATNT FOR REMOVING BUFFERING 
tiles = math.ceil(FrameHeight / bg.get_height()) + 1
# MAIN LOOP 
while 1: 
	# THIS WILL MANAGE THE SPEED OF 
	# THE SCROLLING IN PYGAME 
	clock.tick(60) 

	# APPENDING THE IMAGE TO THE BACK 
	# OF THE SAME IMAGE ---need to change this to
	i = -1
	while(i < 1): 
		screen.blit(bg, (0, bg.get_height()*i + scroll)) 
		i += 1
	# speed
	scroll += 6

	# RESET THE SCROLL FRAME 
	if abs(scroll) > bg.get_height(): 
		scroll = 0
	# CLOSINF THE FRAME OF SCROLLING 
	for event in py.event.get(): 
		if event.type == py.QUIT: 
			quit() 

	py.display.update() 

py.quit() 
