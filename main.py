from raylib import *
from pyray import *
from os.path import join


def main():
    init_window(400, 200, 'fitness app')
    set_target_fps(60)
    show_message_box = False
    

    while not window_should_close():

        begin_drawing()
        clear_background(GRAY)

        if gui_button(Rectangle(24, 24, 120, 30), "#191#show message"):
            show_message_box = True
        
        if show_message_box:
            result = GuiMessageBox(Rectangle(85, 70, 250, 100), bytes('#191#message box', 'utf-8'), bytes('This is a message!', 'utf-8'), (bytes('nice;cool;whatever', 'utf-8')))
            if result >= 0:
                show_message_box = False





        end_drawing()

    close_window()









if __name__ == '__main__':
    main()