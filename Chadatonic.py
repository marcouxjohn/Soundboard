import sys, os
sys.path.insert(0, os.path.abspath('..'))

import pygame, pygbutton
from Elements import Background

from pygame.locals import *

# Frame rate
fps = 30

# Window dimesions
d_width = 800
d_height = 500

# Button sizes
# menuButtons
wm = 125
hm = 65

# playButtons
wp = 90
hp = 65

# Button coordinates
# Rows
row1 = 50
row2 = 140
row3 = 230
row4 = 320
row5 = 410

# Columns
col1 = 25 # menu buttons only
col2 = 220
col3 = 330
col4 = 440
col5 = 550
col6 = 660

dark = (84,20,20)
light = (244,160,49)
white = (225,225,225)

def main():
    windowBgColor = white

    pygame.init()
    fps_clock = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode((d_width,d_height))
    BackGround = Background('bg.png', [0,0])
    pygame.display.set_caption('Chadatonic V1.0')

    # buttons that change the window background color
    overwrite = pygbutton.PygButton((col1, row1, wm, hm), 'Overwrite', bgcolor=light, fgcolor=dark)
    saveNew = pygbutton.PygButton((col1, row2, wm, hm), 'SaveNew', bgcolor=light, fgcolor=dark)
    load = pygbutton.PygButton((col1, row3, wm, hm), 'Load', bgcolor=light, fgcolor=dark)

    menuButtons = (overwrite, saveNew, load)

    # buttons that change the button background color
    b1 = pygbutton.PygButton((col2, row1, wp, hp), '1', bgcolor=light, fgcolor=dark)
    b2 = pygbutton.PygButton((col2, row2, wp, hp), '2', bgcolor=light, fgcolor=dark)
    b3 = pygbutton.PygButton((col2, row3, wp, hp), '3', bgcolor=light, fgcolor=dark)
    b4 = pygbutton.PygButton((col2, row4, wp, hp), '4', bgcolor=light, fgcolor=dark)
    b5 = pygbutton.PygButton((col2, row5, wp, hp), '5', bgcolor=light, fgcolor=dark)

    b6 = pygbutton.PygButton((col3, row1, wp, hp), '6', bgcolor=light, fgcolor=dark)
    b7 = pygbutton.PygButton((col4, row1, wp, hp), '7', bgcolor=light, fgcolor=dark)
    b8 = pygbutton.PygButton((col5, row1, wp, hp), '8', bgcolor=light, fgcolor=dark)
    b9 = pygbutton.PygButton((col6, row1, wp, hp), '9', bgcolor=light, fgcolor=dark)

    playButtons = (b1, b2, b3, b4, b5, b6, b7, b8, b9)

    allButtons = menuButtons + playButtons

    while True: # main game loop
        for event in pygame.event.get(): # event handling loop

            # Quit event
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # MenuButton click events
            if 'click' in overwrite.handleEvent(event):
                windowBgColor = white

            if 'click' in saveNew.handleEvent(event):
                windowBgColor = white

            if 'click' in load.handleEvent(event):
                windowBgColor = white

            # PlayButton click events
            if 'click' in b1.handleEvent(event):
                windowBgColor = white

            if 'click' in b2.handleEvent(event):
                windowBgColor = white

            if 'click' in b3.handleEvent(event):
                windowBgColor = white

            if 'click' in b4.handleEvent(event):
                windowBgColor = white

            if 'click' in b5.handleEvent(event):
                windowBgColor = white

            if 'click' in b6.handleEvent(event):
                windowBgColor = white

            if 'click' in b7.handleEvent(event):
                windowBgColor = white

            if 'click' in b8.handleEvent(event):
                windowBgColor = white

            if 'click' in b9.handleEvent(event):
                windowBgColor = white

        # Display elements in window
        gameDisplay.fill(windowBgColor)

        gameDisplay.blit(BackGround.image, BackGround.rect)

        for b in allButtons:
            b.draw(gameDisplay)

        pygame.display.update()
        fps_clock.tick(fps)


if __name__ == '__main__':
    main()
