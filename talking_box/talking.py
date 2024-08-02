import pygame
import pygame.font
import sys
import os
import math
import random
import numpy
from random import randint
from matplotlib import pyplot as plt
from pygame.locals import *

pygame.init()
w = 1280
h = 720
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

fontpath = "data/fonts/"
font = pygame.font.Font(fontpath + 'font.ttf', 20)

#VARIABLES
display_text = [[]]
full_text = list('Hi. This i a test for a Youtube video. Please leave a like and a subscription if you want to see more of this videos. Enjoy!')
lettercount = 0
skiptalk = False

main = True
while main:
    clock.tick(60)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();sys.exit
            main = False
                    
        if event.type == pygame.KEYDOWN:
            if event.key == 32:
#SKIP
                length = 0
                for i in range(len(display_text)):
                    length += len(display_text[i])
                if length < len(full_text):
                    skiptalk = True
                else:
                    full_text = []
                    display_text = [[]]
                    lettercount = 0
                    skiptalking = False
#LOGIC
    if main:
        if len(full_text) > 0:
            while True:
                length = 0
                for i in range(len(display_text)):
                    length += len(display_text[i])
                if length < len(full_text):
                    display_text[len(display_text) - 1].append(full_text[lettercount])
                    lettercount += 1
                    txt = font.render("".join(map(str, display_text[len(display_text) - 1])), 1, (255, 255, 255))
                    width = txt.get_width()
                    if width > 410:
                        display_text.append([])
                    if not skiptalk:
                        break
                else:
                    break

            for i in range(len(display_text)):
                txt = font.render("".join(map(str, display_text[i])), 1, (255, 255, 255))
                screen.blit(txt, (150, 600 + i * 30))

        pygame.display.flip()

                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
                                                                    #
