import pygame

import game_function as gf
from button import Button
from game_stats import GameStats
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    stats = GameStats(ai_settings)

    ship = Ship(ai_settings, screen)

    bullets = Group()

    aliens = Group()

    gf.create_fleet(ai_settings, screen, aliens)

    play_button = Button(ai_settings, screen, 'Play')

    # 开始游戏的循环
    while True:
        gf.check_events(ai_settings, screen, ship, aliens,bullets, stats, play_button)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, aliens, bullets)
            gf.update_aliens(ai_settings,screen, ship, aliens,stats,bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets, stats, play_button)

run_game()