#!/usr/bin/env python

import random, os.path

#import basic pygame modules
import pygame
from pygame.local import *

#check if we can load > standard BMP
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

#game constants

MAX_SHOTS      = 3      #most player bullets onscreen
ALIEN_ODDS     = 20     #chances a new alien appears
BOMB_ODDS      = 69    #chances a new bomb will drop
ALIEN_RELOAD   = 12     #frames between new aliens
SCREENRECT     = Rect(0, 0, 640, 480)
SCORE          = 0

main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
     "loads an image, prepares it for play"
     file = os.path.join(main_dir, 'data', file)
     try:
         surface = pygame.image.load(file)
     except pygame.error:
         raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
     return surface.convert()

def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs

class dummysound:
    def play(self): pass

def load_sound(file):
    if not pygame.mixer: return dummysound()
    file = os.path.join(main_dir, 'data', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound

# to be continued...