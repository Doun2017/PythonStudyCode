import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
import game_functions as gf

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	(ai_settings.screen_width,ai_settings.screen_height))
	# 设置标题
	pygame.display.set_caption("Alien Invasion")
	stats = GameStats(ai_settings)
	# 创建 Play 按钮
	play_button = Button(ai_settings, screen, "Play")
	# 创建一艘飞船
	ship = Ship(ai_settings, screen)
	# 创建一个用于存储子弹的编组
	bullets = Group()
	aliens = Group()
	# 创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# 开始游戏的主循环
	while True:
		gf.check_events(ai_settings, screen, stats, play_button, ship,
			aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()