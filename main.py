from start_screen import *


pg.init()

if __name__ == "__main__":
    run = True
    if mode == "0":
        active = "menu"
    elif mode == "1":
        active = "settings"
    dif = difficult
    while run:
        if active == "menu":
            result = menu_screen()
            if result == 0:
                active = "settings"
            if result == 1:
                active = "game"
            if result == 2:
                run = False

        if active == "game":
            result = start(dif)
            if result == 2:
                run = False
            if result == 1:
                active = "menu"

        if active == "settings":
            result = settings_screen()
            if result == 3:
                run = False
            if result == 2:
                run = False
            if result[0] == 1:
                dif = result[1]
                print(dif)
                active = "menu"


pg.quit()
