import pygame;

class obstacle(pygame.sprite.Sprite):
    """
    Class to manage the obstacles.
    """

    def __init__(self, imgSizeX, imgSizeY, hitBoxSizeX, hitBoxSizeY, img, x, y):
        # Initialize the obstacle sprite
        super().__init__()

        # Create a transparent surface for the obstacle with specified hit box size
        self.image = pygame.Surface([hitBoxSizeX, hitBoxSizeY], pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        # Load the obstacle image
        self.img = pygame.image.load(img)

        # Set the initial position of the obstacle
        self.rect.x = x
        self.rect.y = y

        # Store additional information about the obstacle
        self.imgSizeX = imgSizeX
        self.imgSizeY = imgSizeY
        self.image.blit(self.img, (0, 0))

    def update(self, speed):
        # Update the obstacle position based on the specified speed
        self.rect.y += speed
