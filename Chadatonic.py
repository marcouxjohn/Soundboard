import sys, os
sys.path.insert(0, os.path.abspath('..'))

import pygame, pygbutton
from Elements import Background
from Elements import Slider

from pygame.locals import *

def main():

    pygame.init()

    # Frame rate
    fps = 30

    MainLoop = True
    ConfigLoop = True
    EditLoop = False

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
    orange = (244,160,49)
    blue = (88, 194, 127)
    white = (225,225,225)

    windowBgColor = white

    fps_clock = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode((d_width,d_height))
    ConfigBg= Background('bg.png', [0,0])
    EditBg = Background('edit.png', [0,0])
    pygame.display.set_caption('Chadatonic V1.0')

    # Menu buttons
    overwrite = pygbutton.PygButton((col1, row1, wm, hm), 'Overwrite', bgcolor=orange, fgcolor=dark)
    saveNew = pygbutton.PygButton((col1, row2, wm, hm), 'SaveNew', bgcolor=orange, fgcolor=dark)
    load = pygbutton.PygButton((col1, row3, wm, hm), 'Load', bgcolor=orange, fgcolor=dark)
    bind = pygbutton.PygButton((col1, row3, wm, hm), 'Bind', bgcolor=orange, fgcolor=dark)
    choose = pygbutton.PygButton((col1, row4, wm, hm), 'ChooseSound', bgcolor=orange, fgcolor=dark)
    delete = pygbutton.PygButton((col1, row5, wm, hm), 'Delete', bgcolor=orange, fgcolor=dark)
    back = pygbutton.PygButton((col1, row5, wm, hm), 'Back', bgcolor=orange, fgcolor=dark)

    # Config window menu buttons
    menu1Buttons = (overwrite, saveNew, load, delete)

    # Edit window menu buttons
    menu2Buttons = (overwrite, saveNew, bind, choose, back)

    # Buttons for playing sounds
    b1 = pygbutton.PygButton((col2, row1, wp, hp), 'c 1', bgcolor=orange, fgcolor=dark)
    b2 = pygbutton.PygButton((col2, row2, wp, hp), '2', bgcolor=orange, fgcolor=dark)
    b3 = pygbutton.PygButton((col2, row3, wp, hp), '3', bgcolor=orange, fgcolor=dark)
    b4 = pygbutton.PygButton((col2, row4, wp, hp), '4', bgcolor=orange, fgcolor=dark)
    b5 = pygbutton.PygButton((col2, row5, wp, hp), '5', bgcolor=orange, fgcolor=dark)

    b6 = pygbutton.PygButton((col3, row1, wp, hp), 'c 2', bgcolor=orange, fgcolor=dark)
    b7 = pygbutton.PygButton((col3, row2, wp, hp), '2', bgcolor=orange, fgcolor=dark)
    b8 = pygbutton.PygButton((col3, row3, wp, hp), '3', bgcolor=orange, fgcolor=dark)
    b9 = pygbutton.PygButton((col3, row4, wp, hp), '4', bgcolor=orange, fgcolor=dark)
    b10 = pygbutton.PygButton((col3, row5, wp, hp), '5', bgcolor=orange, fgcolor=dark)

    b11 = pygbutton.PygButton((col4, row1, wp, hp), 'c 3', bgcolor=orange, fgcolor=dark)
    b12 = pygbutton.PygButton((col4, row2, wp, hp), '2', bgcolor=orange, fgcolor=dark)
    b13 = pygbutton.PygButton((col4, row3, wp, hp), '3', bgcolor=orange, fgcolor=dark)
    b14 = pygbutton.PygButton((col4, row4, wp, hp), '4', bgcolor=orange, fgcolor=dark)
    b15 = pygbutton.PygButton((col4, row5, wp, hp), '5', bgcolor=orange, fgcolor=dark)

    b16 = pygbutton.PygButton((col5, row1, wp, hp), 'c 4', bgcolor=orange, fgcolor=dark)
    b17 = pygbutton.PygButton((col5, row2, wp, hp), '2', bgcolor=orange, fgcolor=dark)
    b18 = pygbutton.PygButton((col5, row3, wp, hp), '3', bgcolor=orange, fgcolor=dark)
    b19 = pygbutton.PygButton((col5, row4, wp, hp), '4', bgcolor=orange, fgcolor=dark)
    b20 = pygbutton.PygButton((col5, row5, wp, hp), '5', bgcolor=orange, fgcolor=dark)

    b21 = pygbutton.PygButton((col6, row1, wp, hp), 'c 5', bgcolor=orange, fgcolor=dark)
    b22 = pygbutton.PygButton((col6, row2, wp, hp), '2', bgcolor=orange, fgcolor=dark)
    b23 = pygbutton.PygButton((col6, row3, wp, hp), '3', bgcolor=orange, fgcolor=dark)
    b24 = pygbutton.PygButton((col6, row4, wp, hp), '4', bgcolor=orange, fgcolor=dark)
    b25 = pygbutton.PygButton((col6, row5, wp, hp), '5', bgcolor=orange, fgcolor=dark)

    # Buttons for editing sounds
    loopb = pygbutton.PygButton((col2, row3, wm, hm), 'Loop', bgcolor=blue, fgcolor=dark)
    filb = pygbutton.PygButton((col5, row3, wm, hm), 'Filter', bgcolor=blue, fgcolor=dark)
    conb = pygbutton.PygButton((col2, row4, wm, hm), 'Concatinate', bgcolor=blue, fgcolor=dark)
    layb = pygbutton.PygButton((col5, row4, wm, hm), 'Layer', bgcolor=blue, fgcolor=dark)

    vol = Slider("Volume", 0, 20, -20, col2)
    amp = Slider("Amplitude", 0, 20, -20, col5)

    playButtons = (b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14,
                   b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25)

    changeButtons = (loopb, filb, conb, layb)

    changeSlider = (vol, amp)


    ConfigButtons = menu1Buttons + playButtons

    EditButtons = menu2Buttons + changeButtons

    while MainLoop: # main game loop

        for event in pygame.event.get(): # event handling loop

            if ConfigLoop:

                bg = ConfigBg
                buttons = ConfigButtons
                #sliders = False

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

                if 'click' in delete.handleEvent(event):
                    windowBgColor = white

                # PlayButton click events
                if 'click' in b1.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b2.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b3.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b4.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b5.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b6.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b7.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b8.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b9.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b10.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b11.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b12.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b13.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b14.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b15.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b16.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b17.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b18.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b19.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b20.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b21.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b22.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b23.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b24.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

                if 'click' in b25.handleEvent(event):
                    if event.button == 3:
                        ConfigLoop = False
                        EditLoop = True
                    windowBgColor = white

            if EditLoop:

                bg = EditBg
                buttons = EditButtons
                #sliders = True

                # Quit event
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                # MenuButton click events
                if 'click' in overwrite.handleEvent(event):
                    windowBgColor = white

                if 'click' in saveNew.handleEvent(event):
                    windowBgColor = white

                if 'click' in bind.handleEvent(event):
                    windowBgColor = white

                if 'click' in choose.handleEvent(event):
                    windowBgColor = white

                if 'click' in back.handleEvent(event):
                    ConfigLoop = True
                    EditLoop = False

                # EditButton and EditSlider click events
            #    if event.type == pygame.MOUSEBUTTONDOWN:
            #       pos = pygame.mouse.get_pos()
            #       for s in changeSlider:
            #           if s.button_rect.collidepoint(pos):
            #              s.hit = True
            #    elif event.type == pygame.MOUSEBUTTONUP:
            #        for s in changeSlider:
            #            s.hit = False

                if 'click' in loopb.handleEvent(event):
                    windowBgColor = white

                if 'click' in filb.handleEvent(event):
                    windowBgColor = white

                if 'click' in conb.handleEvent(event):
                    windowBgColor = white

                if 'click' in layb.handleEvent(event):
                    windowBgColor = white

        # Display elements in window
        gameDisplay.fill(windowBgColor)

        gameDisplay.blit(bg.image, bg.rect)

        for b in buttons:
            b.draw(gameDisplay)

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == '__main__':
    main()