import time
import pygame
import random
import button
import car
import obstacle
#CONSTANTS
SCREENS = ["MainMenu","Game","Instructions", "GameOver"]
LaneXList = [260, 465, 681]

CAR_Y = 495
#IMAGES
#All assets including music were AI generated from Microsoft Copilot and then run through a pixel art filter in Adobe Photoshop 

CarIMG = "Assets/car"+str(random.randint(1,3))+".png"
Cactus1IMG = "Assets/cactus1.png"
Cactus1IMGSize = (81,140)
Cactus2IMG = "Assets/cactus2.png"
Cactus2IMGSize = (78,158)
BarricadeIMG = "Assets/barricade.png"
BarricadeIMGSize = (131,65)
greenShrubIMG = "Assets/greenShrub.png"
greenShrubIMGSize = (119,85)
purpleShrubIMG = "Assets/purpleShrub.png"
purpleShrubIMGSize = (96,71)
BlankBackgroundIMG = "Assets/Blank-Background.png"
BackgroundIMG = "Assets/Background.png"
playButtonIMG = "Assets/play.png"
quitButtonIMG = "Assets/quit.png"
instructionsButtonIMG = "Assets/instructions.png" 
instructionsPageIMG = "Assets/instructionsPage.png"
backButtonIMG = "Assets/back.png"
endScreenIMG = "Assets/endscreen.png"

#SPRITES
carDimensions = (90,179)
car = car.car(carDimensions[0],carDimensions[1],carDimensions[0],carDimensions[1],CarIMG,LaneXList[1],CAR_Y,0)
carGroup = pygame.sprite.Group()
carGroup.add(car)
obstacleGroup = pygame.sprite.Group()
#INITIALIZE PYGAME
class game():
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Set up game attributes and resources
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Vroom")
        self.font = pygame.font.Font(None, 36)
        self.font.set_bold(True)
        self.title = pygame.font.Font(None, 56)
        self.title.set_bold(True)
        self.heading = pygame.font.Font(None, 72)
        self.MoveSpeed = 6
        self.deathcount = 0
        self.death = False
        self.OBJECT_FREQUENCY = 70
        self.OBJECT_FREQUENCY_UP = 350
        FrameHeight = 900
        FrameWidth = 1024
        self.events = 0
        self.screen = pygame.display.set_mode((FrameWidth, FrameHeight))
        pygame.mixer.init()
        pygame.mixer.music.load("Assets/MidnightDrive.mp3")
        # Load images
        self.bg = pygame.image.load(BackgroundIMG).convert()
        self.instructionsPage = pygame.image.load(instructionsPageIMG).convert()
        self.blankbg = pygame.image.load(BlankBackgroundIMG).convert()
        self.endbg = pygame.image.load("Assets/endscreen.png").convert()
        self.ScreenValue = "MainMenu"

        # BUTTONS
        # Define button positions and dimensions
        playButtonPosition = (343, 710)
        playButtonDimensions = (336, 154)
        quitButtonPosition = (343, 770)
        quitButtonDimensions = (335, 86)
        instructionsButtonPosition = (5, 779)
        instructionsButtonDimensions = (266, 112)
        backButtonPosition = (470, 787)
        backButtonDimensions = (335, 86)

        # Create button instances
        PlayButton = button.button(playButtonDimensions[0], playButtonDimensions[1], playButtonDimensions[0],
                                   playButtonDimensions[1], playButtonIMG, playButtonPosition[0], playButtonPosition[1], self.playGame)
        QuitButton = button.button(quitButtonDimensions[0], quitButtonDimensions[1], quitButtonDimensions[0],
                                   quitButtonDimensions[1], quitButtonIMG, quitButtonPosition[0], quitButtonPosition[1], self.quit)
        InstructionButton = button.button(instructionsButtonDimensions[0], instructionsButtonDimensions[1],
                                          instructionsButtonDimensions[0], instructionsButtonDimensions[1], instructionsButtonIMG,
                                          instructionsButtonPosition[0], instructionsButtonPosition[1], self.ShowInstuctions)
        BackButton = button.button(backButtonDimensions[0], backButtonDimensions[1], backButtonDimensions[0],
                                   backButtonDimensions[1], backButtonIMG, backButtonPosition[0], backButtonPosition[1], self.backToMain)

        # Create button groups
        self.MainButtonGroup = pygame.sprite.Group()
        self.InstructionButtonGroup = pygame.sprite.Group()
        self.ExitButtonGroup = pygame.sprite.Group()

        # Add buttons to groups
        self.MainButtonGroup.add(PlayButton)
        self.MainButtonGroup.add(InstructionButton)
        self.InstructionButtonGroup.add(BackButton)
        self.ExitButtonGroup.add(QuitButton)

        # Scene Functions
        self.scroll = 0
        self.score = 0
    def ShowInstuctions(self):
        # Switch to the instructions screen
        self.ScreenValue = "Instructions"
    def playGame(self):
        # Start the game
        self.ScreenValue = "Game"
        #play music
        pygame.mixer.music.play(-1)
    def backToMain(self):
        # Return to the main menu
        self.ScreenValue = "MainMenu"
    def generateObstacle(self, LaneXList):
        # Generate a random obstacle and return it
        obstacleType = random.randint(1, 5)
        lane = random.randint(-1, 1)
        if obstacleType == 1:
            ob = obstacle.obstacle(Cactus1IMGSize[0], Cactus1IMGSize[1], Cactus1IMGSize[0], Cactus1IMGSize[1],
                                   Cactus1IMG, LaneXList[lane + 1], -100)
        elif obstacleType == 2:
            ob = obstacle.obstacle(Cactus2IMGSize[0], Cactus2IMGSize[1], Cactus2IMGSize[0], Cactus2IMGSize[1],
                                   Cactus2IMG, LaneXList[lane + 1], -100)
        elif obstacleType == 3:
            ob = obstacle.obstacle(BarricadeIMGSize[0], BarricadeIMGSize[1], BarricadeIMGSize[0], BarricadeIMGSize[1],
                                   BarricadeIMG, LaneXList[lane + 1], -100)
        elif obstacleType == 4:
            ob = obstacle.obstacle(greenShrubIMGSize[0], greenShrubIMGSize[1], greenShrubIMGSize[0], greenShrubIMGSize[1],
                                   greenShrubIMG, LaneXList[lane + 1], -100)
        elif obstacleType == 5:
            ob = obstacle.obstacle(purpleShrubIMGSize[0], purpleShrubIMGSize[1], purpleShrubIMGSize[0],
                                   purpleShrubIMGSize[1], purpleShrubIMG, LaneXList[lane + 1], -100)

        return ob
    def quit(self):
        # Quit the game
        pygame.quit()
        exit()
    def mainMenu(self, events):
        # Display the main menu
        self.screen.blit(self.bg, (0, 0))
        self.MainButtonGroup.draw(self.screen)
        self.MainButtonGroup.update(events)
    def instructionsMenu(self):
        # Display the instructions menu
        self.screen.blit(self.instructionsPage, (0, 0))
        self.InstructionButtonGroup.draw(self.screen)
        self.InstructionButtonGroup.update(self.events)
    def gameVisuals(self,objGroup):
        #this code from here
        i = -1
        while(i < 1): 
            self.screen.blit(self.blankbg, (0, self.blankbg.get_height()*i + self.scroll)) 
            i += 1
        if not self.death:
            self.scroll += self.MoveSpeed

        if abs(self.scroll) > self.blankbg.get_height(): 
            self.scroll = 0
        #to here is for the scrolling background  i made it using inspiration from the code found here https://www.geeksforgeeks.org/creating-a-scrolling-background-in-pygame/
        if self.death:
            pygame.mixer.music.stop()
            text = self.title.render("Game Over", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.x = 410
            text_rect.y = 300
            self.screen.blit(text, text_rect)
            for car in carGroup:
                    
                    animationstage  = self.deathcount// 10
                    car.setIMG("Assets/boom/boom"+str(animationstage)+".png")
            carGroup.update(self.events, LaneXList)
            carGroup.draw(self.screen)
            objGroup.draw(self.screen)
            return

        carGroup.draw(self.screen)
        carGroup.update(self.events, LaneXList)
        text = self.font.render("Score: "+str(self.score), True, (255, 255, 255))  # RGB values for black
        text_rect = text.get_rect()
        text_rect.x = 10
        text_rect.y = 10
        self.screen.blit(text, text_rect)
        objGroup.draw(self.screen)
        objGroup.update(self.MoveSpeed)
    def gameOver(self):   
        self.screen.blit(self.endbg, (0,0)) 
        self.ExitButtonGroup.draw(self.screen)
        self.ExitButtonGroup.update(self.events)
        text = self.heading.render(str(self.score), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.x = 520
        text_rect.y = 710
        self.screen.blit(text, text_rect)
        #MAIN LOOP
    def run(self):
        while True:
            self.screen.fill((0, 0, 0))  # RGB values for black    
            self.clock.tick(60)    
            self.events = pygame.event.get()
            for event in self.events: 
                if event.type == pygame.QUIT: 
                    quit() 
            if self.ScreenValue == "MainMenu":
                self.mainMenu(self.events)
            elif self.ScreenValue == "Game":
                self.score += 1
                #this code generates the obstacles every OBJECT_FREQUENCY frames
                if self.score % self.OBJECT_FREQUENCY == 0:
                    ob = self.generateObstacle(LaneXList)
                    obstacleGroup.add(ob)
                #this code increases the amount of objects every OBJECT_FREQUENCY_UP frames such that more obstacles spawn the further you get into the game
                if self.score % self.OBJECT_FREQUENCY_UP == 0:
                    self.OBJECT_FREQUENCY -=2
                #checks if car has collided with obstacle
                collisions = pygame.sprite.groupcollide(carGroup, obstacleGroup, False, False)
                if collisions != {}:
                    self.death = True
                if self.death:
                    self.deathcount += 1
                if(self.deathcount == 1):
                    for car in carGroup:
                        car.death()
                self.gameVisuals(obstacleGroup)
                if self.deathcount >= 180:
                    time.sleep(0.1)
                    self.ScreenValue = "GameOver"
            elif self.ScreenValue == "Instructions":
                self.instructionsMenu()
            elif self.ScreenValue == "GameOver":
                self.gameOver()
            else:
                print("Screen not found")
            pygame.display.flip()
        py.quit() 

game = game()
game.run()