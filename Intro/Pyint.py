'''
Created  on Jul, 06 2021

@author: jmhuertasg
'''

import pygame
import os

width, height = 800, 600

FPS = 60

GScreen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game 1")
PICTURE = pygame.image.load(os.path.join('resource', 'cars-png.png'))
SONG = os.path.join(os.getcwd(), 'resource/song_dua.mp3')


def draw_fn():
    GScreen.fill((255,0,255))
    GScreen.blit(PICTURE , (0,0))

    pygame.display.update()

def main():

    pygame.mixer.init()
    pygame.mixer.music.load(SONG)
    pygame.mixer.play

    run =True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        draw_fn()

        #GScreen.fill((255,0,255))
        #pygame.display.update()



if __name__ == "__main__" :
    main()