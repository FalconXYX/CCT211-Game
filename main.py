import math
import time
import pygame
import random
import button
import car
import obstacle
#Global Variables
MoveSpeed = 6
global ScreenValue
ScreenValue = "MainMenu"
#CONSTANTS
SCREENS = ["MainMenu","Game","Instructions", "GameOver"]
LaneXList = [260, 465, 681]
OBJECT_FREQUENCY = 70
OBJECT_FREQUENCY_UP = 350
CAR_Y = 495
#IMAGES
CarIMG = "Assets/car"+str(random.randint(1,3))+".png"
Cactus1IMG = "Assets/cactus1.png"
Cactus1IMGSize = (98,160)
Cactus2IMG = "Assets/cactus2.png"
Cactus2IMGSize = (106,190)
BarricadeIMG = "Assets/barricade.png"
BarricadeIMGSize = (131,70)
greenShrubIMG = "Assets/greenShrub.png"
greenShrubIMGSize = (135,107)
purpleShrubIMG = "Assets/purpleShrub.png"
purpleShrubIMGSize = (117,96)
BlankBackgroundIMG = "Assets/Blank-Background.png"
BackgroundIMG = "Assets/Background.png"
playButtonIMG = "Assets/play.png"
instructionsButtonIMG = "Assets/instructions.png" 
instructionsPageIMG = "Assets/instructionsPage.png"
backButtonIMG = "Assets/back.png"

#FUNCTIONS
def ShowInstuctions ():
    global ScreenValue

    ScreenValue = "Instructions"
def playGame():
    global ScreenValue
    ScreenValue = "Game"
def backToMain():
    global ScreenValue
    ScreenValue = "MainMenu"
def generateObstacle(LaneXList):
    obstacleType = random.randint(1,5)
    lane = random.randint(-1,1)
    if obstacleType == 1:
        ob = obstacle.obstacle(Cactus1IMGSize[0],Cactus1IMGSize[1],Cactus1IMGSize[0],Cactus1IMGSize[1],Cactus1IMG,LaneXList[lane+1],-100)
    elif obstacleType == 2:
        ob = obstacle.obstacle(Cactus2IMGSize[0],Cactus2IMGSize[1],Cactus2IMGSize[0],Cactus2IMGSize[1],Cactus2IMG,LaneXList[lane+1],-100)
    elif obstacleType == 3:
        ob = obstacle.obstacle(BarricadeIMGSize[0],BarricadeIMGSize[1],BarricadeIMGSize[0],BarricadeIMGSize[1],BarricadeIMG,LaneXList[lane+1],-100)
    elif obstacleType == 4:
        ob = obstacle.obstacle(greenShrubIMGSize[0],greenShrubIMGSize[1],greenShrubIMGSize[0],greenShrubIMGSize[1],greenShrubIMG,LaneXList[lane+1],-100)
    elif obstacleType == 5:
        ob = obstacle.obstacle(purpleShrubIMGSize[0],purpleShrubIMGSize[1],purpleShrubIMGSize[0],purpleShrubIMGSize[1],purpleShrubIMG,LaneXList[lane+1],-100)
    
    return ob

#BUTTONS
playButtonPosition = (343,710)
playButtonDimensions = (336,154)
PlayButton = button.button(playButtonDimensions[0],playButtonDimensions[1],playButtonDimensions[0],playButtonDimensions[1],playButtonIMG,playButtonPosition[0],playButtonPosition[1],playGame)

instructionsButtonPosition = (5,779)
instructionsButtonDimensions = (266,112)
InstructionButton = button.button(instructionsButtonDimensions[0],instructionsButtonDimensions[1],instructionsButtonDimensions[0],instructionsButtonDimensions[1],instructionsButtonIMG,instructionsButtonPosition[0],instructionsButtonPosition[1],ShowInstuctions)

backButtonPosition = (470,787)
backButtonDimensions = (335,86)
BackButton = button.button(backButtonDimensions[0],backButtonDimensions[1],backButtonDimensions[0],backButtonDimensions[1],backButtonIMG,backButtonPosition[0],backButtonPosition[1],backToMain)

MainButtonGroup = pygame.sprite.Group()
InstructionButtonGroup = pygame.sprite.Group()
MainButtonGroup.add(PlayButton)
MainButtonGroup.add(InstructionButton)
InstructionButtonGroup.add(BackButton)

#SPRITES
carDimensions = (107,216)
car = car.car(carDimensions[0],carDimensions[1],carDimensions[0],carDimensions[1],CarIMG,LaneXList[1],CAR_Y,0)
carGroup = pygame.sprite.Group()
carGroup.add(car)

obstacleGroup = pygame.sprite.Group()
#INITIALIZE PYGAME
pygame.init() 
clock = pygame.time.Clock()
pygame.display.set_caption("Vroom") 
font = pygame.font.Font(None, 36) 
font.set_bold(True)
FrameHeight = 900
FrameWidth = 1024
screen = pygame.display.set_mode((FrameWidth, 
							FrameHeight)) 
# IMAGE 
bg = pygame.image.load(BackgroundIMG).convert()
instructionsPage = pygame.image.load(instructionsPageIMG).convert()
blankbg = pygame.image.load(BlankBackgroundIMG).convert()
#Scene Functions
scroll = 0
score = 0
def mainMenu(events):

    screen.blit(bg, (0,0)) 
    MainButtonGroup.draw(screen)
    MainButtonGroup.update(events)
    

def instructionsMenu(events):
    screen.blit(instructionsPage, (0,0)) 
    InstructionButtonGroup.draw(screen)
    InstructionButtonGroup.update(events)
def gameVisuals(s,objGroup,d):
    global scroll
    #this code from here
    i = -1
    while(i < 1): 
        screen.blit(blankbg, (0, blankbg.get_height()*i + scroll)) 
        i += 1
    if not d:
        scroll += MoveSpeed

    if abs(scroll) > blankbg.get_height(): 
        scroll = 0
    #to here is for the scrolling background  i made it using inspiration from the code found here https://www.geeksforgeeks.org/creating-a-scrolling-background-in-pygame/
    if d:
        text = font.render("Game Over", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.x = 500
        text_rect.y = 800
        screen.blit(text, text_rect)
        for car in carGroup:
            car.death()
        carGroup.draw(screen)
        return

    carGroup.draw(screen)
    carGroup.update(events, LaneXList)
    text = font.render("Score: "+str(s), True, (0, 0, 0))  # RGB values for black
    text_rect = text.get_rect()
    text_rect.x = 10
    text_rect.y = 10
    screen.blit(text, text_rect)
    objGroup.draw(screen)
    objGroup.update(MoveSpeed)
    

#scene Manager
    
#MAIN LOOP

while True:
    screen.fill((0, 0, 0))  # RGB values for black

    # Update the display
    
    clock.tick(60)
    #print(pygame.mouse.get_pos())  
    
    events = pygame.event.get()
    for event in events: 
        if event.type == pygame.QUIT: 
            quit() 
    if ScreenValue == "MainMenu":
        mainMenu(events)
    elif ScreenValue == "Game":
        score += 1;
        if score % OBJECT_FREQUENCY == 0:
            ob = generateObstacle(LaneXList)
            obstacleGroup.add(ob)
        if score % OBJECT_FREQUENCY_UP == 0:
            OBJECT_FREQUENCY -=2
        collisions = pygame.sprite.groupcollide(carGroup, obstacleGroup, False, False)

        death = False

        if collisions != {}:
            death = True
        else:
            pass

        gameVisuals(score,obstacleGroup, death)
        
        if death:
            time.sleep(1)
            ScreenValue = "GameOver"
        
        
        

    elif ScreenValue == "Instructions":
        
        instructionsMenu(events)
    elif ScreenValue == "GameOver":
        pass
        #gameOver()
    else:
        print("Screen not found")
    #screen.blit(pygame.image.load(CarIMG),pygame.mouse.get_pos())
    pygame.display.flip()
             
       

py.quit() 