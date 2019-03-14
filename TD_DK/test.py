import pygame, sys
import pygame.locals as const
pygame.init()

son = pygame.mixer.Sound(r"pygame\tests\TD_DK\samba.wav")
ecran = pygame.display.set_mode((500, 350))

joue = 0
while 1:
    for event in pygame.event.get():
        if event.type == const.QUIT:                              
            sys.exit()
        if event.type == const.KEYDOWN and event.key == const.K_SPACE and joue == 0:
            son.play()
            joue = 1
        elif event.type == const.KEYDOWN and event.key == const.K_SPACE and joue == 1:
            pygame.mixer.unpause()
        elif event.type == const.KEYUP and event.key == const.K_SPACE:
            pygame.mixer.pause()
        elif event.type == const.KEYDOWN and event.key == const.K_RETURN:
            son.stop()
            joue = 0
