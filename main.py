import math
import pygame
import random

#Golbal Variables
global MoveSpeed
MoveSpeed = 6


#IMAGES
CarIMG = "Assets/car"+str(random.randint(1,3))+".png"
Cactus1IMG = "Assets/cactus1.png"
Cactus2IMG = "Assets/cactus2.png"
BarricadeIMG = "Assets/barricade.png"
greenShrubIMG = "Assets/greenShrub.png"
purpleShrubIMG = "Assets/purpleShrub.png"
BlankBackgroundIMG = "Assets/Blank-Background.png"
BackgroundIMG = "Assets/Background.png"
playButtonIMG = "Assets/play.png"
playButtonPosition = (343,710)
instructionsButtonIMG = "Assets/instructions.png"
instructionsButtonPosition = (5,779)
#INITIALIZE PYGAME
pygame.init() 
clock = pygame.time.Clock() 
pygame.display.set_caption("Vroom") 

FrameHeight = 900
FrameWidth = 1024
screen = pygame.display.set_mode((FrameWidth, 
							FrameHeight)) 

# IMAGE 
bg = pygame.image.load(BackgroundIMG).convert()
#script that get the x and y  of the mouse then prints it
while True:
        clock.tick(60)
        screen.blit(bg, (0,0))
        
        print(pygame.mouse.get_pos())
        screen.blit(pygame.image.load(instructionsButtonIMG),pygame.mouse.get_pos())
        pygame.display.update() 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                quit() 
py.quit() 