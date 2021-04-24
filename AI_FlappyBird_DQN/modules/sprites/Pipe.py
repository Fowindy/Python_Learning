'''
功能描述:
        定义pipe class类模块
作者:
    Fowindy
微信:
    17786508658
github:
       https://github.com/Fowindy/Python_Learning.git
创建时间:
        2020年3月19日 星期四 16:07:30 
'''
#import os #导入os模块：负责程序和操作系统之间的交互
import random # 导入random模块:用于生成管道中的随机变量
import pygame # 导入pygame模块:用于管道界面的设计和显示
'''pipe class'''
class Pipe(pygame.sprite.Sprite):# 新建pipe class类继承精灵序列图实现动画
	def __init__(self, image, position, type_, **kwargs):# 初始化精灵序列图
		pygame.sprite.Sprite.__init__(self) # 调用基类的init方法
		self.image = image # 为图片属性赋值
		self.rect = self.image.get_rect() # 获取图片的尺寸为显示区域赋值
		self.mask = pygame.mask.from_surface(self.image) # 将图片设为封面
		self.rect.left, self.rect.top = position # 为显示区域的左上角赋值当前位置座标
		self.type_ = type_ # 类型参数默认即可
		self.used_for_score = False # 默认是否使用分数为False
	@staticmethod
    # 随机生成管道图像_高度_间距
	def randomPipe(cfg, image):
		base_y = 0.79 * cfg.SCREENHEIGHT
		up_y = int(base_y * 0.2) + random.randrange(0, int(base_y * 0.6 - cfg.PIPE_GAP_SIZE))
		return {'top': (cfg.SCREENWIDTH+10, up_y-image.get_height()), 'bottom': (cfg.SCREENWIDTH+10, up_y+cfg.PIPE_GAP_SIZE)}



