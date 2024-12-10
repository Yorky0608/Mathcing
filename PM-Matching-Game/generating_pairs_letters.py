import pygame
import random

# Generate pairs of symbols (for a memory matching game)
def generate_pairs_letters():
    symbols_face_up = [pygame.image.load("Cards/a.png").convert(), pygame.image.load("Cards/b.png").convert(), pygame.image.load("Cards/c.png").convert(),
                       pygame.image.load("Cards/h.png").convert(), pygame.image.load("Cards/l.png").convert(), pygame.image.load("Cards/p.png").convert(),
                       pygame.image.load("Cards/s.png").convert(), pygame.image.load("Cards/w.png").convert()] * 2  # 8 unique symbols, each appearing twice
    random.shuffle(symbols_face_up)
    return symbols_face_up