#import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((100, 100))

path = 'data/test.png'
layers = 15
img = pygame.image.load(path).convert_alpha()
w, h = img.get_size()

for i in range(layers):
    subsurface = pygame.Surface((w, h / layers), pygame.SRCALPHA)
    subsurface.blit(img, (0, -h / layers * i))
    pygame.image.save(subsurface, 'data/' + f'test_{layers - i:03}.png')

pygame.quit()



