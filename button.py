import pygame

class button(pygame.sprite.Sprite):
    """
    Class to manage the buttons.
    """

    def __init__(self, imgSizeX, imgSizeY, hitBoxSizeW, hitBoxSizeH, img, x, y, function):
        # Initialize the button sprite
        super().__init__()

        # Create a transparent surface for the button with specified size
        self.image = pygame.Surface([imgSizeX, imgSizeY], pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        # Load the button image
        self.img = pygame.image.load(img)

        # Set the position of the button
        self.rect.x = x
        self.rect.y = y

        # Store additional information about the button
        self.imgSizeX = imgSizeX
        self.imgSizeY = imgSizeY
        self.function = function

        # Draw the button image on the button surface
        self.image.blit(self.img, (0, 0))

    def update(self, events):
        # Update the button based on events
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                # Check if the mouse click is within the button's rectangle
                if self.rect.collidepoint(event.pos):
                    # Trigger the button click event
                    self.click()

    def click(self):
        # Execute the assigned function when the button is clicked
        if self.function:
            self.function()
