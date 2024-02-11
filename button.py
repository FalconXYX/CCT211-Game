import pygame
class button(pygame.sprite.Sprite):
    """
    Class to manage the buttons.
    """

    def __init__(self,imgSizeX,imgSizeY, hitBoxSizeW, hitBoxSizeH, img, x, y, function):
        super().__init__()

        self.image = pygame.Surface([imgSizeX, imgSizeY],pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.img = pygame.image.load(img)
        self.rect.x = x
        self.rect.y = y
        self.imgSizeX = imgSizeX
        self.imgSizeY = imgSizeY
        self.function = function
        self.image.blit(self.img,(0,0));  



    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.click()
                    
    def click(self):
        if self.function:
            self.function()

