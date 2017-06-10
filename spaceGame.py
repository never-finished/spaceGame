#this is the main program loop which uses the other files to create the game

import pygame
from gameSettings import Settings
import game_functions as gf
from shp import Ship
from pygame.sprite import Group
#from star import Star 

s1 = Settings()
screen = pygame.display.set_mode((s1.screen_width,s1.screen_height))
ship = Ship(s1, screen)


def run_game():
    #initialize game
    pygame.init()
    pygame.display.set_caption("Aliens Attack")
    bullets = Group() 
    aliens = Group()
    gf.create_fleet(s1, screen, aliens)
    
    #main loop
    while True:
        #imports event handler and checks for events
        gf.check_events(s1, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        #gf.update_stars(stars)
        gf.update_aliens(aliens)
        gf.update_screen(s1, screen, ship, aliens, bullets)
       

run_game()
