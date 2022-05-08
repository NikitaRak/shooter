from classes import *
from random import randint
import os
from pygame import mixer
''' Фон '''
background = transform.scale(image.load(os.path.join(MEDIA_DIR, 'background.jpg')), (win_rez_x, win_rez_y))
''' Игрок '''
player = Unit(os.path.join(MEDIA_DIR, 'x-wing.png'), win_rez_x / 2 - units_size / 2, win_rez_y * 7 / 8,
              units_size, 5)
''' Снаряды '''
def bullet_generate():
    bullets.append(Unit(os.path.join(MEDIA_DIR, 'Bullet.png'), player.rect.x + units_size // 2 - bullets_size // 2,
                        player.rect.y, bullets_size, 15))

bullets = []
''' Враги '''
def enemy_generate():
    enemies.append(Unit(os.path.join(MEDIA_DIR, 'CID.png'), randint(0, win_rez_x - units_size), 0,
                        units_size, 2))

enemies = []
''' Фонт '''
font.init()
font = font.SysFont('Arial', 70)
score = 0
score_font = font.render('SCORE:' + str(score), True, (185, 155, 155))

def update_score(score):
    return font.render('SCORE:' + str(score), True, (185, 155, 155))

''' Музыка '''
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play