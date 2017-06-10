class Settings():
   def __init__(self):
        #screen size
        self.screen_width = 1200
        self.screen_height = 800
        #color format R, G, B for background 
        self.bg_color = (0,250,0)
        #speeds of game
        self.player_speed = 3.5
        self.enemy_speed = 2
        self.alien_descent = .1
        #shooting settings
        self.bullet_speed = 6
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250,100,0)
        self.max_bullets = 3

        #if we want to calculate max aliens use code below and comment out the number input below
        #alien = Enemy(s1, screen)
        #alien_width = alien.rect.width
        #available_spacex = s1.screen.width - 2 * alien_width
        #number_aliensx = int(available_spacex / (2*alien_width))
        self.number_aliensx = 3
        self.number_rows = 3

        #star details
        #self.star_speed = 1
        self.star_width = 5
        self.star_height = 5
        self.star_color = (250,250,250)