import pygame, os, sys, random
from CONST import *
from player import *
from enemy import Enemy

class Game():
    def __init__(self):
        pygame.init()

        self.load_textures()
        # self.load_sounds()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.draw_screen = pygame.Surface(DRAW_SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.dt = 1

        self.game()

    def load_textures(self):
        self.textures = {}
        for img in os.listdir("img"):
            texture = pygame.image.load("img/" + img)
            self.textures[img.replace(".png", "")] = texture

    #    # def load_sounds(self):
    #     pass
    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()
            if event.type ==self.ENEMYMOVE:
                for enemy in self.enemies:
                    enemy.move()

    def check_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.player.x += int(round(PLAYER_SPEED * self.dt))
        if keys[pygame.K_LEFT]:
            self.player.x -= int(round(PLAYER_SPEED * self.dt))
        if keys[pygame.K_SPACE]:
            pass

    def close(self):
        pygame.quit()
        sys.exit(0)

    def game(self):
        self.ENEMYMOVE = pygame.USEREVENT
        pygame.time.set_timer(self.ENEMYMOVE, MOVE_RATIO)

        self.enemies = []
        for y in range(3):
            for x in range(int(DRAW_SCREEN_SIZE[0] - (BORDER * 2)/42)):
                enemy = Enemy(x * 40, y * 20, y + 1)
                self.enemies.append(enemy)

        self.player = Player()
        self.projectile = []

        while True:
            self.check_keys()
            self.check_event()

            for projectile in self.projectiles:
                if projectile.y < 0 or projectile.y > DRAW_SCREEN_SIZE[1]:
                    self.projectiles.remove(projectile)



            self.draw()
            self.refresh_screen()
            scaled = pygame.transform.scale(self.draw_screen, SCREEN_SIZE)
            self.screen.blit(scaled, (0, 0))
            pygame.display.update()
            self.dt = self.clock.tick(FRAMERATE) * FRAMERATE / 1000

    def draw(self):
        self.draw_screen.blit(self.textures["background"], (0,0))
        self.draw_screen.blit(self.textures["player"], self.player)
        for enemy in self.enemies:
            self.draw_screen.blit(self.textures["enemy" + enemy.type], enemy)
        for projectile in self.projectile:
            self.draw_screen.blit(self.textures["projectile" + projectile.type], projectile)


    def refresh_screen(self):
        pass


Game()
