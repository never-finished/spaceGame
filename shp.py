import pygame

class Ship():
    def __init__(self, s1, screen):
        self.screen = screen
        self.s1 = s1
        self.image = pygame.image.load("Ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #sets starting position
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        #sets up a movement flag so if true we move, default to false
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        #moves ship if the flag is true and if we aren't going off the screen
        if self.moving_left and self.rect.left > 0:
            self.center -= self.s1.player_speed      
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.s1.player_speed

        self.rect.centerx = self.center
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)



