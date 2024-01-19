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
        self.image.blit(self.img,(self.imgSizeX,self.imgSizeY));
        self.lane = lane;


        
        
    def move(self, direction: int, laneXList):
        if(self.lane == -1):
            if(direction == 1):
                self.rect.x = laneXList[1]
                self.lane = 0
            elif(direction == -1):
                return False
        if(self.lane == 0):
            if(direction == 1):
                self.rect.x = laneXList[2]
                self.lane = 1
            elif(direction == -1):
                self.rect.x = laneXList[0]
                self.lane = -1
            return True
        if(self.lane == 1):
            if(direction == 1):
                return False
            elif(direction == -1):
                self.rect.x = laneXList[1]
                self.lane = 0
    
