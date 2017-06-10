import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    def __init__(self, s1, screen):
        #creates stars starting form the top of the screen
        super().__init__()
        self.screen = screen    
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0,0,s1.star_width,s1.star_height)
        self.selfx = randint(0,s1.screen_height)
        self.selfy = randint(0,s1.screen_width)
        self.rect.centerx = self.selfx
        self.rect.centery = self.selfy
        self.color = s1.star_color
        
        
    
    # this is to move starts top of sceen to bottom
    #self.rect.top = self.screen_rect.top
    #self.star_speed = s1.star_speed
    #def update(self):
    #    self.y -= self.star_speed
    #    self.rect.y = self.y

    def draw_star(self):
        for i in range(0,20):
            pygame.draw.rect(self.screen, self.color, self.rect)


