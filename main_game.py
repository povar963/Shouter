from settings_screen import *

pg.init()
bullets = pg.sprite.Group()
enemies = pg.sprite.Group()
player_group = pg.sprite.Group()
f1 = pg.font.Font(None, int(screen.get_width() / 20))


class Tile(pg.sprite.Sprite):
    imgs = [pg.image.load("./txtures/bg2.png")]

    def __init__(self, x, y):
        super().__init__(*[tiles, all_sprites])
        self.image = self.imgs[random.randint(0, 0)]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.rect.bottom < 0 or self.rect.right < 0:
            self.kill()
        if self.rect.top > screen.get_height() or self.rect.left > screen.get_width():
            self.kill()



class Enemy(pg.sprite.Sprite):
    img = pg.image.load("txtures/1.png")

    def __init__(self, player):
        super().__init__(*[all_sprites, enemies])
        self.image = self.img
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = -1000
        self.player = player
        self.is_alive = False

    def create(self):
        x = random.randint(70, screen.get_width() - 70)
        y = random.randint(70, screen.get_height() - 70)
        self.rect.x = x
        self.rect.y = y

        while pg.sprite.collide_mask(self, self.player):
            x = random.randint(70, screen.get_width() - 70)
            y = random.randint(70, screen.get_height() - 70)
            self.rect.x = x
            self.rect.y = y

        self.counter = 100
        self.is_alive = True

    def shoot(self):
        x = self.rect.center[0]
        y = self.rect.center[1]
        BulletE(x=x, y=y, player=self.player)

    def watch(self):
        x = self.rect.center[0]
        y = self.rect.center[1]
        mouse_x, mouse_y = self.player.rect.center
        rel_x, rel_y = mouse_x - x, mouse_y - y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pg.transform.rotate(self.img, int(angle))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        if self.is_alive:
            self.watch()
            if self.player.alive():
                if shoot_enemy:
                    if self.counter <= 0:
                        self.shoot()
                        self.counter = 100
                    elif self.counter > 0:
                        self.counter -= 1
            else:
                self.kill()


class BulletE(pg.sprite.Sprite):
    img = pg.image.load("txtures/Bullet.png")

    def __init__(self, x, y, player):
        super().__init__(*[all_sprites, bullets])
        mouse_x, mouse_y = player.rect.center
        rel_x, rel_y = mouse_x - x, mouse_y - y
        self.angle = math.atan2(rel_y, rel_x)
        self.speed = player_speed

        self.xm = self.speed * math.cos(self.angle)
        self.ym = self.speed * math.sin(self.angle)

        self.image = pg.transform.rotate(self.img, -math.degrees(self.angle))
        self.rect = self.image.get_rect(center=(x, y))

        self.player = player

    def update(self):
        self.rect.x += self.xm
        self.rect.y += self.ym
        if not (-2000 < self.rect.x < 2000 and -2000 < self.rect.y < 2000):
            self.kill()
        if pg.sprite.collide_mask(self, self.player):
            self.player.health -= 1
            self.kill()


class BulletF(pg.sprite.Sprite):
    img = pg.image.load("txtures/Bullet.png")

    def __init__(self, x, y):
        super().__init__(*[bullets, all_sprites])
        mouse_x, mouse_y = pg.mouse.get_pos()
        rel_x, rel_y = mouse_x - x, mouse_y - y
        self.angle = math.atan2(rel_y, rel_x)
        self.speed = 20

        self.xm = self.speed * math.cos(self.angle)
        self.ym = self.speed * math.sin(self.angle)

        self.image = pg.transform.rotate(self.img, -math.degrees(self.angle))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.x += self.xm
        self.rect.y += self.ym
        if not (-100 < self.rect.x < screen.get_width() + 100 and -100 < self.rect.y < screen.get_height() + 100):
            self.kill()
        for enemy in enemies:
            if pg.sprite.collide_mask(self, enemy):
                enemy.kill()
                self.kill()


class Player(pg.sprite.Sprite):
    img = pg.image.load("txtures/gg.png")
    f1 = pg.font.Font(None, 36)

    def __init__(self, diff):
        super().__init__(player_group)
        self.health = max_health
        self.difficult = diff
        self.max_health = max_health
        self.image = self.img
        self.rect = self.image.get_rect()
        self.speed = 5
        self.counter = 0
        self.def_counter = 100
        self.rect.x = screen.get_width() / 2 - self.rect.width / 2
        self.rect.y = screen.get_height() / 2 - self.rect.height / 2

    def watch(self):
        x = self.rect.center[0]
        y = self.rect.center[1]
        mouse_x, mouse_y = pg.mouse.get_pos()
        rel_x, rel_y = mouse_x - x, mouse_y - y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pg.transform.rotate(self.img, int(angle))
        self.rect = self.image.get_rect(center=(x, y))

    def heath_bar(self):
        fx = self.rect.center[0] - 60
        lx = self.rect.center[0] + 60
        fy = self.rect.center[1] - 100
        pg.draw.line(screen, "DarkRed", (fx, fy), (lx, fy), 10)
        fx = self.rect.center[0] - 58
        lx = fx + (116 * (self.health / self.max_health))
        pg.draw.line(screen, "red", (fx, fy), (lx, fy), 6)
        fx = fx - 20
        lx = fx + 10
        if self.counter == 0:
            pg.draw.line(screen, "green", (fx, fy), (lx, fy), 10)
        else:
            pg.draw.line(screen, "red", (fx, fy), (lx, fy), 10)
        text1 = f1.render(f"hp:{round(self.health, 2)} cd:{self.counter}", 1, (180, 0, 0))
        screen.blit(text1, (10, screen.get_height() - f1.get_height()))

    def laser(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        x, y = self.rect.center
        pg.draw.line(screen, "red", (x, y), (mouse_x, mouse_y), 10)

    def shoot(self):
        x = self.rect.center[0]
        y = self.rect.center[1]
        if self.counter <= 0:
            BulletF(x=x, y=y)
            self.counter = self.def_counter

    def control(self, key):
        if key[pg.K_w]:
            for sprite in all_sprites:
                sprite.rect.y += self.speed
            start_tile_pos[1] -= self.speed
        if key[pg.K_s]:
            for sprite in all_sprites:
                sprite.rect.y -= self.speed
            start_tile_pos[1] += self.speed
        if key[pg.K_d]:
            for sprite in all_sprites:
                sprite.rect.x -= self.speed
            start_tile_pos[0] += self.speed
        if key[pg.K_a]:
            for sprite in all_sprites:
                sprite.rect.x += self.speed
            start_tile_pos[0] -= self.speed

    def update(self):
        keys = pg.key.get_pressed()
        mouse = pg.mouse.get_pressed()
        self.control(keys)
        self.watch()
        if keys[pg.K_LALT]:
            self.laser()
        if shoot_player:
            if keys[pg.K_SPACE] or mouse[0]:
                self.shoot()
        if self.counter > 0:
            self.counter -= 1
        if self.health <= 0:
            self.health = 0
            self.kill()


def create_list(factor, player):
    factor += 0.5
    quantity = [10, 15]
    random_value = random.randint(int(quantity[0]), int(quantity[1]))
    enemies_spawn = []
    for i in range(int(random_value * factor)):
        enemies_spawn.append(Enemy(player=player))
    return enemies_spawn


def fill_bg():
    for tile in tiles:
        tile.kill()
    count_x = round(screen.get_width() / Tile.imgs[0].get_width() + 0.4)
    count_y = round(screen.get_height() / Tile.imgs[0].get_height() + 0.4)
    dx = round((0 - start_tile_pos[0]) / Tile.imgs[0].get_width() + 0.4)
    dy = round((0 - start_tile_pos[1]) / Tile.imgs[0].get_height() + 0.4)
    for i in range(count_y + 1):
        for j in range(count_x + 1):
            x = j * Tile.imgs[0].get_width() - start_tile_pos[0]
            y = i * Tile.imgs[0].get_height() - start_tile_pos[1]
            Tile(x - dx * Tile.imgs[0].get_width(), y - dy * Tile.imgs[0].get_height())


def start(diff):
    global spawn_queue

    player = Player(diff)
    start_time = time.time()
    clock = pg.time.Clock()
    healing_timing = 0
    elapsed = 0
    spawn_period = 0
    factor = 3
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 2
        if True:  # Run
            if spawn_toggle:  # Spawn
                if int(elapsed) == spawn_period:
                    spawn_queue = create_list(factor, player)
                    countdown_queue = []
                    period = int(50 * factor)
                    spawn_period += int(50 * factor)
                    factor += 0.1
                    for i in range(len(spawn_queue)):
                        count = i + 1
                        time_spawn = spawn_period - period + (period / len(spawn_queue) * count)
                        countdown_queue.append(round(time_spawn, 1))
                if spawn_queue:
                    if round(elapsed, 1) in countdown_queue:
                        i = countdown_queue.index(round(elapsed, 1))
                        spawn_queue[i].create()
                        countdown_queue.pop(i)
                        spawn_queue.pop(i)

            if heal_allowed:
                if player.health <= max_health:
                    if healing_timing == int(elapsed):
                        if player.health + heal / diff <= max_health:
                            player.health += heal / diff
                            healing_timing = int(elapsed) + healing_timer
                        else:
                            player.health = max_health

                else:
                    healing_timing = int(elapsed) + healing_timer
            #Отрисовка bg
            fill_bg()
            tiles.draw(screen)
            tiles.update()
            # Отрисовка Врагов
            enemies.update()
            enemies.draw(screen)
            # Отрисовка Снарядов
            bullets.update()
            bullets.draw(screen)
            #Отрисовка Игрока
            player_group.update()
            player_group.draw(screen)
            if player.alive():
                player.heath_bar()
                elapsed = time.time() - start_time
            else:
                w = int(screen.get_height() / 3)
                fy = int(screen.get_height() / 3) + w / 2
                f2 = pg.font.Font(None, int(w / 2))
                pg.draw.line(screen, "black", (0, fy), (screen.get_width(), fy), w)
                text_end = f2.render(f"Lose", 1, (180, 0, 0))
                screen.blit(text_end,
                            (int(screen.get_width() / 2 - text_end.get_width() / 2), fy - text_end.get_height() / 2))
                keys = pg.key.get_pressed()
                if keys[pg.K_SPACE]:
                    return 0
                elif keys[pg.K_ESCAPE]:
                    return 1
            text_seconds = f1.render(f"{int(elapsed)}", 1, (180, 0, 0))
            screen.blit(text_seconds, (screen.get_width() / 2 - text_seconds.get_width(), 10))
            pg.display.flip()
        clock.tick(75)