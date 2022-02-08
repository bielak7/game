import pygame, os, sys, random
from CONST import *
from player import *


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
    def check_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += 1
        if keys[pygame.K_LEFT]:
            pass
        if keys[pygame.K_SPACE]:
            pass

    def close(self):
        pygame.quit()
        sys.exit(0)

    def game(self):

        self.player = Player()

        while True:
            self.check_keys()
            self.check_event()
            self.draw()
            self.refresh_screen()
            scaled = pygame.transform.scale(self.draw_screen, SCREEN_SIZE)
            self.screen.blit(scaled, (0, 0))
            pygame.display.update()
            self.dt = self.clock.tick(FRAMERATE) * FRAMERATE / 1000

    def draw(self):
        pass

    def refresh_screen(self):
        pass


Game()
