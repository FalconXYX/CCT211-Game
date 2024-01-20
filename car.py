import pygame;
class car(pygame.sprite.Sprite):
    """
    Class to manage the car.
    """

    def __init__(self,imgSizeX,imgSizeY, hitBoxSizeX, hitBoxSizeY, img, x, y,lane):
        super().__init__()

        self.image = pygame.Surface([hitBoxSizeX, hitBoxSizeY],pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.img = pygame.image.load(img)
        self.rect.x = x
        self.rect.y = y
        self.imgSizeX = imgSizeX
        self.imgSizeY = imgSizeY
        self.image.blit(self.img,(0,0));
        self.lane = lane;


    def update(self, events, laneXList):
        for event in events:
            #if the event is a keypress
            if event.type == pygame.KEYDOWN:
                #if the key is the left arrow
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    #move the car left
                    self.move(-1, laneXList)
                #if the key is the right arrow
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    #move the car right
                    self.move(1, laneXList)
        
    def move(self, direction: int, laneXList):
        if(self.lane == -1):
            if(direction == 1):
                self.rect.x = laneXList[1]
                self.lane = 0
            elif(direction == -1):
                return False
        elif(self.lane == 0):
            if(direction == 1):
                self.rect.x = laneXList[2]
                self.lane = 1
            elif(direction == -1):
                self.rect.x = laneXList[0]
                self.lane = -1
            return True
        elif(self.lane == 1):
            if(direction == 1):
                return False
            elif(direction == -1):
                self.rect.x = laneXList[1]
                self.lane = 0
    def death(self):
        self.img = pygame.image.load("Assets/boom.png")
        self.image.blit(self.img,(0,0));
    
