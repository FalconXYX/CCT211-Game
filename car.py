import pygame;

class car(pygame.sprite.Sprite):
    """
    Class to manage the car.
    """

    def __init__(self, imgSizeX, imgSizeY, hitBoxSizeX, hitBoxSizeY, img, x, y, lane):
        # Initialize the car sprite
        super().__init__()

        # Create a transparent surface for the car with specified hit box size
        self.image = pygame.Surface([hitBoxSizeX, hitBoxSizeY], pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        # Load the car image
        self.img = pygame.image.load(img)

        # Set the initial position of the car
        self.rect.x = x
        self.rect.y = y

        # Store additional information about the car
        self.imgSizeX = imgSizeX
        self.imgSizeY = imgSizeY
        self.image.blit(self.img, (0, 0))
        self.lane = lane

    def update(self, events, laneXList):
        # Update the car based on events and lane information
        for event in events:
            # If the event is a keypress
            if event.type == pygame.KEYDOWN:
                # If the key is the left arrow or 'a'
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    # Move the car left
                    self.move(-1, laneXList)
                # If the key is the right arrow or 'd'
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    # Move the car right
                    self.move(1, laneXList)

    def move(self, direction: int, laneXList):
        # Move the car in the specified direction within the lanes
        if self.lane == -1:
            if direction == 1:
                self.rect.x = laneXList[1]
                self.lane = 0
            elif direction == -1:
                return False
        elif self.lane == 0:
            if direction == 1:
                self.rect.x = laneXList[2]
                self.lane = 1
            elif direction == -1:
                self.rect.x = laneXList[0]
                self.lane = -1
            return True
        elif self.lane == 1:
            if direction == 1:
                return False
            elif direction == -1:
                self.rect.x = laneXList[1]
                self.lane = 0

    def setIMG(self, img):
        # Set a new image for the car
        self.img = pygame.image.load(img)
        self.image = pygame.Surface([192, 192], pygame.SRCALPHA)
        self.image.blit(self.img, (0, 0))

    def death(self):
        # Move the car left when it encounters an obstacle (death condition)
        self.rect.x -= 50
