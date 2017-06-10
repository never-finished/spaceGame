import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, s1, screen):
        super(Enemy, self).__init__()
        self.screen = screen
        self.s1 = s1
        self.image = pygame.image.load("UFO.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #sets starting position
        self.rect.x = self.rect.width
        self.x = float(self.rect.x)
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)
        #sets up a movement flag so if true we move, default to false
        self.moving_right = True
        self.moving_left = False
    
    def update(self):
        #moves ship if the flag is true and if we aren't going off the screen        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.s1.enemy_speed
        else:
            self.moving_right = False
            self.moving_left = True
        if self.moving_left and self.rect.left > 0:
            self.x -= self.s1.enemy_speed  
        else:
            self.moving_right = True
            self.moving_left = False
            self.y += self.s1.alien_descent

        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        

