import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

class Bucket(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.image.load("catbed.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))

    # Get the rectangle of the surface
        self.rect = self.image.get_rect()

        self.rect.x = 290
        self.rect.y = 600

        self.baseSpeed = 3

    def moveRight(self, baseSpeed):
        if self.rect.x + 30 <= SCREEN_WIDTH: 
            self.rect.x += baseSpeed
            

    def moveLeft(self, baseSpeed):
        if self.rect.x >= 0:
            self.rect.x -= baseSpeed

    def moveUp(self, baseSpeed):
        if self.rect.y + 30 >= 0:
            self.rect.y -= baseSpeed
    
    def moveDown(self, baseSpeed):
        if self.rect.y + 30 <= SCREEN_HEIGHT:
            self.rect.y += baseSpeed
            
    def resetBucket(self):
        self.rect.x = 290
        self.rect.y = 600