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
import os #导入os模块：负责程序和操作系统之间的交互
import random # 导入random模块:用于生成管道中的随机变量
import pygame # 导入pygame模块:用于管道界面的设计和显示
'''pipe class'''
class Pipe(pygame.sprite.Sprite) # 新建pipe class类继承精灵序列图实现动画