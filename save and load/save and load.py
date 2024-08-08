# save and load

#pip install joblib

import pygame
import sys
import joblib

pygame.init()
w = 1280
h = 720
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

#VARIABLES
try:
    (playerx, playery) = joblib.load('data/save/' + 'save_file1.joblib')
except:
    playerx = 100
    playery = 100
xvel = 0
yvel = 0

#FUNCTIONS
main = True
while main:
    clock.tick(30)
    screen.fill((230, 230, 230))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            joblib.dump((playerx, playery), 'data/save/' + 'save_file1.joblib')
            pygame.quit();sys.exit
            main = False
        elif event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                xvel = -5
            elif event.key == ord('d'):
                xvel = 5
            elif event.key == ord('w'):
                yvel = -5
            elif event.key == ord('s'):
                yvel = 5
        elif event.type == pygame.KEYUP:
            if event.key == ord('a'):
                xvel = 0
            elif event.key == ord('d'):
                xvel = 0
            elif event.key == ord('w'):
                yvel = 0
            elif event.key == ord('s'):
                yvel = 0

    
#LOGIC
    if main:
        playerx += xvel
        playery += yvel

        pygame.draw.rect(screen, (20, 20, 150), pygame.Rect(playerx, playery, 50, 50), 0)

        pygame.display.flip()
