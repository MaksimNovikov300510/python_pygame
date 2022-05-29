#Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import os

# настройка папки ассетов
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder, 'maleAdventurer.png'))
player2_img = pygame.image.load(os.path.join(img_folder, 'zombie.png'))

WIDTH = 1530 # ширина игрового окна
HIGHT = 800 # высота игрового окна
FPS = 30 # частота кадров в секунду

#color
Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2,HIGHT / 2)
    def update(self):
        self.rect.x +=5
        if self.rect.left > WIDTH:
            self.rect.right = 0

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player2_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2,HIGHT / 2)
    def update(self):
        self.rect.x +=4
        if self.rect.left > WIDTH:
            self.rect.right = 0
# создаем игру и окно
pygame.init()
pygame.mixer.init() # для звука
screen = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption('шаблон') # название окна
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
player2 = Player2()
all_sprites.add(player2)

# Цикл игры
running = True
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Обновление
    all_sprites.update()
    # Визуализация (сборка)
    screen.fill(Blue)
    all_sprites.draw(screen)

    pygame.display.flip()



   # pygame.quit()