# FILE:     Chadatonic.py
# AUTHOR:   Margaret Perry
# DATE:     2019/11/22
# VERSION:  1.3
# PURPOSE:  User Interface for Chadatonic

import sys, os

sys.path.insert(0, os.path.abspath('..'))

import pygame
from pygame.locals import *
import pygbutton
from main_back import *
from fileFunctions import *
from soundplayer import *
from Elements import Background

"""
Name:        main
Purpose:     Generates soundboard UI
Arguments:   None
Output:      None
Modifies:    None
Returns:     Game window
Assumptions: None
Bugs:        None
"""

def main():

    back = BackEnd()

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

    # Colours for buttons and background
    dark = (84,20,20)
    orange = (244,160,49)
    blue = (88, 194, 127)
    white = (225,225,225)

    windowBgColor = white

    # initalizing frames and window
    fps_clock = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode((d_width,d_height))

    # Initalize backgrounds
    ConfigBg= Background('bg.png', [0,0])
    EditBg = Background('edit.png', [0,0])

    # Makes window title
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
    menu1Buttons = [overwrite, saveNew, load, delete]

    # Edit window menu buttons
    menu2Buttons = [overwrite, saveNew, bind, choose, back]

    # Buttons for playing sounds
    playButtons = []

    for column in range(0,5):
        for rows in range(0,5):
            playButtons.append(pygbutton.PygButton((column*110 + 220, rows*90 + 50, wp, hp), 'c 1', bgcolor=orange, fgcolor=dark))
            



    # Buttons for editing sounds
    # Volume buttons
    volume = pygbutton.PygButton((col2, row1, wm, hm), 'Volume', bgcolor=orange, fgcolor=dark)
    v0 = pygbutton.PygButton((col3+20, row1, wp, hp), '- 10', bgcolor=blue, fgcolor=dark)
    v1 = pygbutton.PygButton((col4+20, row1, wp, hp), '- 5', bgcolor=blue, fgcolor=dark)
    v2 = pygbutton.PygButton((col5+20, row1, wp, hp), '+ 5', bgcolor=blue, fgcolor=dark)
    v3 = pygbutton.PygButton((col6+20, row1, wp, hp), '+ 10', bgcolor=blue, fgcolor=dark)

    # Amplitude buttons
    amp = pygbutton.PygButton((col2, row2, wm, hm), 'Amplitude', bgcolor=orange, fgcolor=dark)
    amp0 = pygbutton.PygButton((col3+20, row2, wp, hp), '- 10', bgcolor=blue, fgcolor=dark)
    amp1 = pygbutton.PygButton((col4+20, row2, wp, hp), '- 5', bgcolor=blue, fgcolor=dark)
    amp2 = pygbutton.PygButton((col5+20, row2, wp, hp), '+ 5', bgcolor=blue, fgcolor=dark)
    amp3 = pygbutton.PygButton((col6+20, row2, wp, hp), '+ 10', bgcolor=blue, fgcolor=dark)



    loopb = pygbutton.PygButton((col2, row3, wm, hm), 'Loop', bgcolor=blue, fgcolor=dark)
    filb = pygbutton.PygButton((col5, row3, wm, hm), 'Filter', bgcolor=blue, fgcolor=dark)
    conb = pygbutton.PygButton((col2, row4, wm, hm), 'Concatenate', bgcolor=blue, fgcolor=dark)
    layb = pygbutton.PygButton((col5, row4, wm, hm), 'Layer', bgcolor=blue, fgcolor=dark)

    # Buttons used for playing sounds
    #playButtons = (b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14,
    #               b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25)

    # Buttons used for editing
    changeButtons = [volume, v0, v1, v2, v3, amp, amp0, amp1, amp2, amp3, loopb, filb, conb, layb]

    # All congiguration buttons
    ConfigButtons = menu1Buttons + playButtons

    # All edit buttons
    EditButtons = menu2Buttons + changeButtons

    # main game loop
    while MainLoop:


        for event in pygame.event.get(): # event handling loop

            # Congiguration screen loop
            if ConfigLoop:

                bg = ConfigBg
                buttons = ConfigButtons

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
                for button in playButtons:
                    if 'click' in button.handleEvent(event):
                        if event.button == 3:
                            ConfigLoop = False
                            EditLoop = True
                            editInit = False
                            currentSound = playButtons.index(button)
                        windowBGColor = white


            # Edit screen loop
            if EditLoop:

                if (not editInit):
                    # Load config for current sound
                    nowName = "Airplane"
                    nowConfig = "Config1"
                    configData = load_sound_config(nowName, nowConfig)
                    editInit = True

                # Get current config settings


                bg = EditBg
                buttons = EditButtons

                # Quit event
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                # MenuButton click events


                # Saving the sound
                if 'click' in overwrite.handleEvent(event):
                    windowBgColor = white
                    save_sound_config(configData, nowConfig)


                # Getting rid of this
                if 'click' in saveNew.handleEvent(event):
                    windowBgColor = white

                if 'click' in bind.handleEvent(event):
                    windowBgColor = white

                if 'click' in choose.handleEvent(event):
                    windowBgColor = white

                if 'click' in back.handleEvent(event):
                    ConfigLoop = True
                    EditLoop = False

                # EditButton click events


                # Volume Control
                # -10
                if 'click' in v0.handleEvent(event):
                    windowBgColor = white
                    configData[1] = configData[1] - 10
                # - 5
                if 'click' in v1.handleEvent(event):
                    windowBgColor = white
                    configData[1] = configData[1] - 5
                # 5
                if 'click' in v2.handleEvent(event):
                    windowBgColor = white
                    configData[1] = configData[1] + 5
                # 10
                if 'click' in v3.handleEvent(event):
                    windowBgColor = white
                    configData[1] = configData[1] + 10

                # -10
                if 'click' in amp0.handleEvent(event):
                    windowBgColor = white
                    configData[2] = configData[2] - 10
                # -5
                if 'click' in amp1.handleEvent(event):
                    windowBgColor = white
                    configData[2] = configData[2] - 5
                # 5
                if 'click' in amp2.handleEvent(event):
                    windowBgColor = white
                    configData[2] = configData[2] + 5
                # 10
                if 'click' in amp3.handleEvent(event):
                    windowBgColor = white
                    configData[2] = configData[2] + 10

                # Loop
                if 'click' in loopb.handleEvent(event):
                    windowBgColor = white
                    configData[3] = not configData[3]

                if 'click' in filb.handleEvent(event):
                    windowBgColor = white
                    configData[5] = not configData[5]

                if 'click' in conb.handleEvent(event):
                    windowBgColor = white

                if 'click' in layb.handleEvent(event):
                    windowBgColor = white

        # Display elements in window
        gameDisplay.fill(windowBgColor)

        # Display background
        gameDisplay.blit(bg.image, bg.rect)

        # Display all buttons
        for b in buttons:
            b.draw(gameDisplay)

        # Updates screen
        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == '__main__':
    main()
