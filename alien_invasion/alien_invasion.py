import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()
    aliens  = Group()

    # 创建一个外星人
    alien = Alien(ai_settings, screen)
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 船舰存储游戏统计信息的实例，并创建积分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 设置背景颜色
    bg_color = (ai_settings.bg_color)
    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        


run_game()
