from main_game import *


class Button_play(Button):
    def update(self):
        self.draw()
        mouse = pg.mouse.get_pressed()
        mouse_x, mouse_y = pg.mouse.get_pos()
        if self.x <= mouse_x <= self.lx + self.x and self.y <= mouse_y <= self.ly + self.y and mouse[0]:
            return 1

class Button_settings(Button):
    def update(self):
        self.draw()
        mouse = pg.mouse.get_pressed()
        mouse_x, mouse_y = pg.mouse.get_pos()
        if self.x <= mouse_x <= self.lx + self.x and self.y <= mouse_y <= self.ly + self.y and mouse[0]:
            return 0


def menu_screen():
    run = True
    button_play = Button_play("Start", "green", 10, screen.get_height() / 2 - 100, 180, 90)
    button_settings = Button_settings("Settings", "green", 10, screen.get_height() / 2 + 10, 180, 90)
    while run:
        screen.fill('black')
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 2
        play_res = button_play.update()
        sett_res = button_settings.update()
        if play_res == 1:
            return 1
        if sett_res == 0:
            return 0
        pg.display.flip()
