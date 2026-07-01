import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from pygame.constants import *
from pygame import (
    display,
    draw,
    image,
    key,
    mouse,
    cursors,
    mask,
    font,
    Rect,
    Surface,
    Cursor,
    Mask,
)
from pygame.display import get_surface, set_mode, set_icon, set_caption
from pygame.font import Font
from pygame.key import get_mods, set_mods, get_pressed
from pygame.time import get_ticks, delay, wait, set_timer, Clock
from pygame.math import *
from pygame.color import THECOLORS, Color
from pygame.sprite import (
    Sprite,
    Group,
    GroupSingle,
    collide_rect,
    collide_rect_ratio,
    collide_circle,
    collide_circle_ratio,
    collide_mask,
    spritecollide,
    spritecollideany,
)
from pygame.transform import (
    scale,
    scale_by,
    rotate,
    rotozoom,
    chop,
    scale2x,
    smoothscale,
    smoothscale_by,
)

if getattr(pygame, "IS_CE", False):
    from pygame.display import message_box # pyright: ignore[reportAttributeAccessIssue]
    from pygame.key import get_just_pressed, get_just_released # pyright: ignore[reportAttributeAccessIssue]
    from pygame.transform import hsl # pyright: ignore[reportAttributeAccessIssue]

import sys
from pathlib import Path
from random import choice, choices, randint, shuffle, uniform
from config import *

pygame.init()

def load_images(folder_path: str = 'assets/images'):
    images = {}
    valid_extensions = ('.bmp', '.gif', '.jpeg', '.lbm', '.pbm', '.pgm', '.ppm', '.pcx', '.png', '.pnm', '.svg', '.tga', '.tiff', '.webp', '.xpm')
    for filename in os.listdir(folder_path):
        if not filename.lower().endswith(valid_extensions): continue
        file_path = os.path.join(folder_path, filename)   
        images[os.path.splitext(filename)[0]] = pygame.image.load(file_path).convert_alpha()
    return images
