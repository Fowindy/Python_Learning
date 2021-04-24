'''
功能描述:
        定义Bird class类模块
作者:
    Fowindy
微信:
    17786508658
github:
       https://github.com/Fowindy/Python_Learning.git
创建时间:
        2020年3月19日 星期四 18:01:24 
'''
#import os #导入os模块：负责程序和操作系统之间的交互
import pygame
import itertools


'''定义鸟类模型'''
class Bird(pygame.sprite.Sprite):
	def __init__(self, images, idx, position, **kwargs):
		pygame.sprite.Sprite.__init__(self)
		self.images = images
		self.image = list(images.values())[idx]
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
		self.rect.left, self.rect.top = position
		# 垂直移动所需的变量
		self.is_flapped = False
		self.speed = -9
		# bird状态所需的开关变量
		self.bird_idx = idx
		self.bird_idx_cycle = itertools.cycle([0, 1, 2, 1])
		self.bird_idx_change_count = 0
	'''更新小鸟的状态'''
	def update(self, boundary_values):
		# 垂直更新位置
		if not self.is_flapped:
			self.speed = min(self.speed+1, 10)
		self.is_flapped = False
		self.rect.top += self.speed
		# 判断这只鸟是不是因为撞到上下边界而死亡
		is_dead = False
		if self.rect.bottom > boundary_values[1]:
			is_dead = True
			self.rect.bottom = boundary_values[1]
		if self.rect.top < boundary_values[0]:
			is_dead = True
			self.rect.top = boundary_values[0]
		# 模拟翅膀动作
		self.bird_idx_change_count += 1
		if self.bird_idx_change_count % 3 == 0:
			self.bird_idx = next(self.bird_idx_cycle)
			self.image = list(self.images.values())[self.bird_idx]
			self.bird_idx_change_count = 0
		return is_dead
	'''设置飞行模式'''
	def setFlapped(self):
		self.is_flapped = True
		self.speed = -9
	'''绑定到屏幕'''
	def draw(self, screen):
		screen.blit(self.image, self.rect)