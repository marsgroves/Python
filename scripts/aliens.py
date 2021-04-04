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

# to be continued...