import sys
import pygame
from bullet import Bullet
from enemies import Enemy
#from star import Star

def check_events(s1, screen, ship, bullets):
    #looks for user inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, s1, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)

def check_keydown(event, s1, screen, ship, bullets):         
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE and len(bullets) < s1.max_bullets:
            new_bullet = Bullet(s1, screen, ship)
            bullets.add(new_bullet)
                          
def check_keyup(event, ship):        
     if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
           ship.moving_right = False
        elif event.key == pygame.K_LEFT:
           ship.moving_left = False

def update_bullets(aliens, bullets):
    bullets.update()
    collission = pygame.sprite.groupcollide(bullets, aliens, True, True )
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_alien(s1, screen, aliens, alien_number, row_number):
    alien = Enemy(s1, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien_height = alien.rect.height
    alien.y = alien_height + 2 * alien_height * row_number
    alien.rect.y = alien.y
    aliens.add(alien)

def create_fleet(s1, screen, aliens):
    for row_number in range(s1.number_rows):
        for alien_number in range(s1.number_aliensx):
            alien = Enemy(s1, screen)    
            create_alien(s1, screen, aliens, alien_number, row_number)

def update_aliens(aliens):
    aliens.update()
    #for alien in aleins.copy():

#this is to create moving stars, at random and move them top to bottom, not finished
#def create_stars(stars): 
#    event1 = False
#    if event1:
#        new_star = Star(s1, screen)
#        stars.add(new_star)
#def update_stars(stars):
#    stars.update()
#    for star in stars.copy():
#        #i need to update 800 to screen height
#        if star.rect.top >= 800:
#            stars.remove(star)


def update_screen(s1, screen, ship, aliens, bullets):
    screen.fill(s1.bg_color)
    ship.blitme()
    aliens.draw(screen)
    #drawing bullets for each one in the group
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #for star in stars.sprites():
    #    star.draw_star()

    #refreshes the screen
    pygame.display.flip()