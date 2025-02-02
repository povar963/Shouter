from settings import *

pg.init()

cur_resolution = resolution
cur_difficult = difficult
pressed = False


class Screen_resolution():
    f1 = pg.font.Font(None, 36)

    def __init__(self):
        self.color = "green"
        self.x = screen.get_width() / 2
        self.y = screen.get_height() / 2

    def draw(self):
        global cur_resolution
        text = f"Разрешение:{cur_resolution[0]}-{cur_resolution[1]}"
        text1 = self.f1.render(text, 1, (0, 180, 0))
        x = self.x - text1.get_width() / 2
        y = self.y - text1.get_height() / 2
        lx = text1.get_width() + 20
        ly = text1.get_height() + 20
        btn = pg.draw.rect(screen, self.color, ((x, y), (lx, ly)), 2)

        tx = btn.width / 2 + x - text1.get_width() / 2
        ty = btn.height / 2 + y - text1.get_height() / 2

        screen.blit(text1, (tx, ty))
        return x, y, lx, ly

    def update(self):
        global pressed
        x, y, lx, ly = self.draw()
        mouse = pg.mouse.get_pressed()
        mouse_x, mouse_y = pg.mouse.get_pos()
        if x <= mouse_x <= lx + x and y <= mouse_y <= ly + y and mouse[0] and not pressed:
            pressed = True
            self.change()
        elif not mouse[0]:
            pressed = False

    def change(self):
        global run, cur_resolution
        resolutions = [(1920, 1080), (1280, 720), (1366, 768)]
        for i in range(len(resolutions)):
            if int(cur_resolution[0]) == resolutions[i][0] and int(cur_resolution[1]) == resolutions[i][1]:
                try:
                    w, h = resolutions[i + 1][0], resolutions[i + 1][1]
                    break
                except IndexError:
                    w, h = resolutions[0][0], resolutions[0][1]
                    break
        cur_resolution = (str(w), str(h))

class Difficult():
    f1 = pg.font.Font(None, 36)

    def __init__(self):
        self.color = "green"
        self.x = screen.get_width() / 2
        self.y = screen.get_height() / 2 + self.f1.get_height() + 40

    def draw(self):
        global cur_resolution
        text = f"Сложность:{difficult}"
        text1 = self.f1.render(text, 1, (0, 180, 0))
        x = self.x - text1.get_width() / 2
        y = self.y - text1.get_height() / 2
        lx = text1.get_width() + 20
        ly = text1.get_height() + 20
        btn = pg.draw.rect(screen, self.color, ((x, y), (lx, ly)), 2)

        tx = btn.width / 2 + x - text1.get_width() / 2
        ty = btn.height / 2 + y - text1.get_height() / 2

        screen.blit(text1, (tx, ty))
        return x, y, lx, ly

    def update(self):
        global pressed
        x, y, lx, ly = self.draw()
        mouse = pg.mouse.get_pressed()
        mouse_x, mouse_y = pg.mouse.get_pos()
        if x <= mouse_x <= lx + x and y <= mouse_y <= ly + y and mouse[0] and not pressed:
            pressed = True
            self.change()
        elif not mouse[0]:
            pressed = False

    def change(self):
        global run, difficult
        diffs = [1, 2, 3]
        for i in range(len(diffs)):
            if difficult == diffs[i]:
                try:
                    dif = diffs[i + 1]
                    break
                except IndexError:
                    dif = diffs[0]
                    break
        difficult = (int(dif))


class Escape_button():
    f1 = pg.font.Font(None, 36)

    def __init__(self):
        self.color = "green"
        self.x = 10
        self.y = 10
        self.text = f"В меню"

    def draw(self):
        text1 = self.f1.render(self.text, 1, (0, 180, 0))
        x = self.x
        y = self.y
        lx = text1.get_width() + 20
        ly = text1.get_height() + 20
        btn = pg.draw.rect(screen, self.color, ((x, y), (lx, ly)), 2)

        tx = btn.width / 2 + x - text1.get_width() / 2
        ty = btn.height / 2 + y - text1.get_height() / 2

        if resolution != cur_resolution:
            text2 = self.f1.render("Игру нужно будет перезапустить", 1, (150, 0, 0))
            screen.blit(text2, (tx + lx, ty))
        screen.blit(text1, (tx, ty))
        return x, y, lx, ly

    def update(self):
        x, y, lx, ly = self.draw()
        mouse = pg.mouse.get_pressed()
        mouse_x, mouse_y = pg.mouse.get_pos()
        if x <= mouse_x <= lx + x and y <= mouse_y <= ly + y and mouse[0]:
            return self.save_changes()

    def save_changes(self):
        if resolution != cur_resolution:
            mode = 1
        else:
            mode = 0
        with open("settings/screen.txt", "w") as f:
            f.write(f"{cur_resolution[0]}-{cur_resolution[1]}-{mode}-{difficult}")
        if resolution != cur_resolution:
            return 2
        else:
            return 1


def settings_screen():
    resolution_button = Screen_resolution()
    run = True
    while run:
        screen.fill("black")
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 2
        resolution_button.update()
        Difficult().update()
        menu_res = Escape_button().update()
        if menu_res == 1:
            return 1, difficult
        if menu_res == 2:
            return 2
        pg.display.flip()
