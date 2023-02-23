import pygame 
from sys import exit
from random import randint


pygame.init()

# Config  (Ability to change game window size, player (aka monster) speed, FPS & more.)
WIDTH = 1000
HEIGHT = 800
SPEED = 10
FPS = 75
SCORE = 0
DOUBLE_BUTTON = True # Lets you use 2 arrow keys at the same time. (Set to "False" to disable it.)
CLOCK = pygame.time.Clock()

# Screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# Monster
monster_surf = pygame.image.load("octopus.png").convert_alpha()
monster_surf_scaled = pygame.transform.scale(monster_surf,(60,60))
monster_rect = monster_surf_scaled.get_rect(center = (WIDTH/2,HEIGHT/2))

# Coin
coin_surf = pygame.image.load("coin.png").convert_alpha()
coin_surf_scaled = pygame.transform.scale(coin_surf,(50,50))
coin_rect = coin_surf_scaled.get_rect(center = (500,500))

# Sky
sky_surf = pygame.image.load("sky.jpg").convert()
sky_surf_scaled = pygame.transform.scale(sky_surf,(WIDTH+200,HEIGHT))
sky_rect = sky_surf_scaled.get_rect(center = (WIDTH/2,HEIGHT/2))

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    button = pygame.key.get_pressed()
    if button[pygame.K_LEFT] and monster_rect.left > 0:
        monster_rect.x -= SPEED
    elif button[pygame.K_RIGHT] and monster_rect.right < WIDTH:
        monster_rect.x += SPEED
    elif button[pygame.K_UP] and monster_rect.top > 0:
        monster_rect.y -= SPEED
    elif button[pygame.K_DOWN] and monster_rect.bottom < HEIGHT:
        monster_rect.y += SPEED
    if DOUBLE_BUTTON:
        if button[pygame.K_LEFT] and monster_rect.left > 0 and button[pygame.K_UP] and monster_rect.top > 0:
            monster_rect.x -= (SPEED/3)
            monster_rect.y -= (SPEED/3)
        elif button[pygame.K_RIGHT] and monster_rect.right < WIDTH and button[pygame.K_UP] and monster_rect.top > 0:
            monster_rect.x += (SPEED/3)
            monster_rect.y -= (SPEED/3)
        elif button[pygame.K_LEFT] and monster_rect.left > 0 and button[pygame.K_DOWN] and monster_rect.bottom < HEIGHT:
            monster_rect.x -= (SPEED/3)
            monster_rect.y += (SPEED/3)
        elif button[pygame.K_RIGHT] and monster_rect.right < WIDTH and button[pygame.K_DOWN] and monster_rect.bottom < HEIGHT:
            monster_rect.x += (SPEED/3)
            monster_rect.y += (SPEED/3)
            
        
    
    # Text/Score
    text_font = pygame.font.Font('Pixeltype.ttf', 50)
    text_surf = text_font.render(f"Score:  {SCORE}",False,"White")
    text_rect = text_surf.get_rect(center = (WIDTH/2,100))
    
    if monster_rect.colliderect(coin_rect):
        coin_rect.x = randint(0,WIDTH-50)
        coin_rect.y = randint(0,HEIGHT-50)
        SCORE += 1

    screen.blit(sky_surf_scaled,sky_rect)
    screen.blit(monster_surf_scaled,monster_rect)
    screen.blit(coin_surf_scaled,coin_rect)
    screen.blit(text_surf,text_rect)
    pygame.display.update()
    CLOCK.tick(FPS)
        