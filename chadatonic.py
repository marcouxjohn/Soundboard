# FILE:     Chadatonic.py
# AUTHOR:   Margaret Perry
# DATE:     2019/11/22
# VERSION:  1.3
# PURPOSE:  User Interface and functonality for Chadatonic

#imports
import sys, os

sys.path.insert(0, os.path.abspath('..'))

import pygame
from pygame.locals import *
import pygbutton
from main_back import *
from fileFunctions import *
from soundplayer import *
from Elements import Background
import random
import mod_sound

# Global var for the current sound bein edited
current_sound = "none"

"""
Name:        main
Purpose:     Generates soundboard wwindow and buttons
Arguments:   None
Output:      None
Modifies:    None
Returns:     Game window
"""

def main():
    pygame.init()
    back_end = BackEnd()

    # Frame rate
    fps = 30

    # Screen loops defined
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
    load = pygbutton.PygButton((col1, row2, wm, hm), 'Load', bgcolor=orange, fgcolor=dark)
    cancel = pygbutton.PygButton((col1, row2, wm, hm), 'CancelChange', bgcolor=orange, fgcolor=dark)
    delete = pygbutton.PygButton((col1, row5, wm, hm), 'Delete', bgcolor=orange, fgcolor=dark)
    back = pygbutton.PygButton((col1, row5, wm, hm), 'Back', bgcolor=orange, fgcolor=dark)

    # Config window menu buttons
    menu1Buttons = [overwrite, load, delete]

    # Edit window menu buttons
    menu2Buttons = [overwrite,cancel, back]

    # Create list of sounds in sounds library
    sounds = []
    for sound in back_end.sound_names:
        sound = sounds.append(sound)

    # Creates list array of buttons and creates buttons for playing sounds
    playButtons = []
    # Used for determining name of the sound assigned to a given button
    temp = 0

    for column in range(0,5):
        for rows in range(0,5):
            playButtons.append(pygbutton.PygButton((column*110 + 220, rows*90 + 50, wp, hp), sounds[temp], bgcolor=orange, fgcolor=dark, font=(pygame.font.Font('freesansbold.ttf', 10))))
            temp = temp+1

    # Buttons for editing sounds
    # Volume buttons
    volume = pygbutton.PygButton((col2, row1, wm, hm), 'Volume', bgcolor=orange, fgcolor=dark)
    v0 = pygbutton.PygButton((col3+20, row1, wp, hp), '- 10', bgcolor=blue, fgcolor=dark)
    v1 = pygbutton.PygButton((col4+20, row1, wp, hp), '- 5', bgcolor=blue, fgcolor=dark)
    v2 = pygbutton.PygButton((col5+20, row1, wp, hp), '+ 5', bgcolor=blue, fgcolor=dark)
    v3 = pygbutton.PygButton((col6+20, row1, wp, hp), '+ 10', bgcolor=blue, fgcolor=dark)

    # Bass buttons
    amp = pygbutton.PygButton((col2, row2, wm, hm), 'Bass', bgcolor=orange, fgcolor=dark)
    amp0 = pygbutton.PygButton((col3+20, row2, wp, hp), '- 10', bgcolor=blue, fgcolor=dark)
    amp1 = pygbutton.PygButton((col4+20, row2, wp, hp), '- 5', bgcolor=blue, fgcolor=dark)
    amp2 = pygbutton.PygButton((col5+20, row2, wp, hp), '+ 5', bgcolor=blue, fgcolor=dark)
    amp3 = pygbutton.PygButton((col6+20, row2, wp, hp), '+ 10', bgcolor=blue, fgcolor=dark)

    loopb = pygbutton.PygButton((col2, row3, wm, hm), 'Loop', bgcolor=blue, fgcolor=dark)
    conb = pygbutton.PygButton((col2, row4, wm, hm), 'Concatenate', bgcolor=blue, fgcolor=dark)

    # Buttons used for editing
    changeButtons = [volume, v0, v1, v2, v3, amp, amp0, amp1, amp2, amp3, loopb, conb]

    # All congiguration buttons
    ConfigButtons = menu1Buttons + playButtons

    # All edit buttons
    EditButtons = menu2Buttons + changeButtons

    # Stops stacking of config modifications
    n_effects = [None, 0, 0, False, 0, False, 0]

    # Main game loop
    while MainLoop:

        for event in pygame.event.get(): # event handling loop

            # Congiguration screen loop
            if ConfigLoop:

                # Change buttons and background
                bg = ConfigBg
                buttons = ConfigButtons

                # Quit event
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                # MenuButton click events
                # Functionality to be added in Chadatonic 2.0
                if 'click' in overwrite.handleEvent(event):
                    windowBgColor = white

                if 'click' in load.handleEvent(event):
                    windowBgColor = white

                if 'click' in delete.handleEvent(event):
                    windowBgColor = white

                # PlayButton click events
                for button in playButtons:
                    if 'click' in button.handleEvent(event):
                        # Right click takes you to the edit page for the given sound
                        if event.button == 3:
                            current_sound = sounds[playButtons.index(button)]
                            ConfigLoop = False
                            EditLoop = True
                            editInit = False
                            currentSound = playButtons.index(button)
                        # Left click will play a sound
                        if sounds[playButtons.index(button)]:
                            back_end.play_sound(sounds[playButtons.index(button)])
                        # else for if no sound is assigned to a button
                        else:
                            print("nice")

            # Edit screen loop
            if EditLoop:

                # Load config for current sound
                if (not editInit):
                    nowConfig = current_sound
                    config_data = load_sound_config(current_sound, nowConfig)
                    editInit = True

                # Change buttons and background
                bg = EditBg
                buttons = EditButtons

                # Quit event
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                # MenuButton click events
                # Go back to config screen
                if 'click' in back.handleEvent(event):
                    ConfigLoop = True
                    EditLoop = False

                # Save edits to sound file
                if 'click' in overwrite.handleEvent(event):
                    save_sound_config(config_data, config_data[0])
                    # Make sound effects happen here
                    mod_sound.apply_effects(config_data[0], n_effects)
                    n_effects = [None, 0, 0, False, 0, False, 0]

                # Cancel edits to sound file
                if 'click' in cancel.handleEvent(event):
                    n_effects = [None, 0, 0, False, 0, False, 0]

                # Volume Control
                # -10
                if 'click' in v0.handleEvent(event):
                    if config_data != -1:
                        config_data[1] = config_data[1] - 10
                        n_effects[1] = n_effects[1] - 10
                # - 5
                if 'click' in v1.handleEvent(event):
                    if config_data != -1:
                       config_data[1] = config_data[1] - 5
                       n_effects[1] = n_effects[1] - 5
                # 5
                if 'click' in v2.handleEvent(event):
                    if config_data != -1:
                        config_data[1] = config_data[1] + 5
                        n_effects[1] = n_effects[1] + 5
                # 10
                if 'click' in v3.handleEvent(event):
                    if config_data != -1:
                        config_data[1] = config_data[1] + 10
                        n_effects[1] = n_effects[1] + 10

                # Bass Control
                # -10
                if 'click' in amp0.handleEvent(event):
                    if config_data != -1:
                        config_data[2] = config_data[2] - 10
                        n_effects[2] = n_effects[2] - 10
                # -5
                if 'click' in amp1.handleEvent(event):
                    if config_data != -1:
                        config_data[2] = config_data[2] - 5
                        n_effects[2] = n_effects[2] - 5
                # 5
                if 'click' in amp2.handleEvent(event):
                    if config_data != -1:
                        config_data[2] = config_data[2] + 5
                        n_effects[2] = n_effects[2] + 5
                # 10
                if 'click' in amp3.handleEvent(event):
                    if config_data != -1:
                        config_data[2] = config_data[2] + 10
                        n_effects[2] = n_effects[2] + 10

                # Loop button 
                if 'click' in loopb.handleEvent(event):
                    config_data[3] = True
                    config_data[4] = config_data[4] + 1
                    n_effects[3] = True
                    n_effects[4] = n_effects[4] + 1

                # Concatenate button
                if 'click' in conb.handleEvent(event):
                    config_data[5] = True
                    config_data[6] = sounds[random.randint(0,24)]
                    n_effects[5] = True
                    n_effects[6] = sounds[random.randint(0,24)]

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
