import pygame
class button(pygame.sprite.Sprite):
    """
    Class to manage the buttons.
    """

    def __init__(self,imgSizeX,imgSizeY, hitBoxSizeX, hitBoxSizeY, img, x, y, function):
        super().__init__()

        self.image = pygame.Surface([hitBoxSizeX, hitBoxSizeY],pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.img = pygame.image.load(img)
        self.rect.x = x
        self.rect.y = y
        self.imgSizeX = imgSizeX
        self.imgSizeY = imgSizeY
        self.function = function
        self.image.blit(self.img,(self.imgSizeX,self.imgSizeY));



        
    def click(self):
        if self.function:
            self.function()
    