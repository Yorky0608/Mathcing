import pygame
import random

# Generate pairs of symbols (for a memory matching game)
def generate_pairs_numbers():
    symbols_face_up = [pygame.image.load("1-8_numbers_images/1.jpg").convert(), pygame.image.load("1-8_numbers_images/2.jpg").convert(),
                       pygame.image.load("1-8_numbers_images/3.jpg").convert(), pygame.image.load("1-8_numbers_images/4.jpg").convert(),
                       pygame.image.load("1-8_numbers_images/5.jpg").convert(), pygame.image.load("1-8_numbers_images/6.jpg").convert(),
                       pygame.image.load("1-8_numbers_images/7.jpg").convert(),
                       pygame.image.load("1-8_numbers_images/8.jpg").convert()] * 2  # 8 unique symbols, each appearing twice
    random.shuffle(symbols_face_up)
    return symbols_face_up