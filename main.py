from start_screen import *

pg.init()

if __name__ == "__main__":
    run = True
    active = "menu"
    while run:
        if active == "menu":
            result = menu_screen()
            if result == 1:
                active = "game"
            if result == 2:
                run = False
        if active == "game":
            result = start()
            if result == 2:
                run = False
            if result == 1:
                active = "menu"


pg.quit()
