# render sprite stack
import pygame
import os
import sys

pygame.init()
w = 1280
h = 720
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
rotation = 0

#IMAGES
path = os.path.join('data')
carimages = [pygame.image.load(os.path.join(path, img)).convert_alpha() for img in os.listdir(path)]
for i in range(len(carimages)):
    width, height = carimages[i].get_size()
    carimages[i] = pygame.transform.scale(carimages[i], (width * 8, height * 8))

#FUNCTIONS
def render_image(images, x, y, rotation, spreadx, spready):
    rot = pygame.transform.rotate(images[0], rotation)
    sprite_sheet = pygame.Surface((rot.get_width() + len(images) * spreadx, rot.get_height() + len(images) * spready), pygame.SRCALPHA)
    for i, img in enumerate(images):
        rot = pygame.transform.rotate(img, rotation)
        sprite_sheet.blit(rot, (i * spreadx, sprite_sheet.get_height() - rot.get_height() - i * spready))
    sprite_sheet.convert_alpha()
    screen.blit(sprite_sheet, (x - sprite_sheet.get_width() / 2, y - sprite_sheet.get_height() / 2))

main = True
while main:
    clock.tick(30)
    screen.fill((230, 230, 230))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();sys.exit
            main = False
    rotation += 2

#LOGIC
    if main:
        render_image(carimages, w/2, h/2, rotation, 0, 1)         
             
        pygame.display.flip()
