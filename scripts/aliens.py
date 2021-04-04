#!/usr/bin/env python

import random, os.path

#import basic pygame modules
import pygame
from pygame.local import *

#check if we can load > standard BMP
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")