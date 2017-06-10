import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, s1, screen, ship):
        #creates bullet starting form the ships current position
        super().__init__()
        self.screen = screen
    
        self.rect = pygame.Rect(0,0,s1.bullet_width, s1.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store position as float because we can
        self.y = float(self.rect.y)
        #attributes are set in s1 which is settings
        self.color = s1.bullet_color
        self.bullet_speed = s1.bullet_speed

    def update(self):
        self.y -= self.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)