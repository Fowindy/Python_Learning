'''
功能描述:
        游戏界面相关配置参数
作者:
    Fowindy
微信:
    17786508658
github:
       https://github.com/Fowindy/Python_Learning.git
创建时间:
        2020年03月19日 13:32:43   
'''
import os #导入os模块：负责程序和操作系统之间的交互
# 定义屏幕刷新的帧率参数FPS
FPS = 30
# 定义屏幕尺寸宽和高
SCREENWIDTH = 288
SCREENHEIGHT = 512
# 定义管道出现的间距
PIPE_GAP_SIZE = 100
# 定义数字图片路径
NUMBER_IMAGE_PATHS = {
                        '0':os.path.join(os.getcwd(),'resources/images/0.png'),
                        '1':os.path.join(os.getcwd(),'resources/images/1.png'),
                        '2':os.path.join(os.getcwd(),'resources/images/2.png'),
                        '3':os.path.join(os.getcwd(),'resources/images/3.png'),
                        '4':os.path.join(os.getcwd(),'resources/images/4.png'),
                        '5':os.path.join(os.getcwd(),'resources/images/5.png'),
                        '6':os.path.join(os.getcwd(),'resources/images/6.png'),
                        '7':os.path.join(os.getcwd(),'resources/images/7.png'),
                        '8':os.path.join(os.getcwd(),'resources/images/8.png'),
                        '9':os.path.join(os.getcwd(),'resources/images/9.png'),
                      }
# 定义小鸟图片路径
BIRD_IMAGE_PATHS = {
                    # 定义红色的鸟
                    'red':{
                            # 定义小鸟翅膀_上的图片
                            'up':os.path.join(os.getcwd(),'resources/images/redbird-upflap.png'),
                            # 定义小鸟翅膀_中的图片
                            'mid':os.path.join(os.getcwd(),'resources/images/redbird-midflap.png'),
                            # 定义小鸟翅膀_下的图片
                            'down':os.path.join(os.getcwd(),'resources/images/redbird-downflap.png'),
                        },
                    # 定义蓝色的小鸟
                    'blue':{
                        'up':os.path.join(os.getcwd(),'resources/images/bluebird-upflap.png'),
                        'mid':os.path.join(os.getcwd(),'resources/images/bluebird-midflap.png'),
                        'down':os.path.join(os.getcwd(),'resources/images/bluebird-downflap.png')
                        },
                    # 定义黄色的小鸟
                    'yellow':{
                        'up':os.path.join(os.getcwd(),'resources/images/yellowbird-upflap.png'),
                        'mid':os.path.join(os.getcwd(),'resources/images/yellowbird-midflap.png'),
                        'down':os.path.join(os.getcwd(),'resources/images/yellowbird-downflap.png')
                        }
                    }
# 定义背景图片路径
BACKGROUND_IMAGE_PATHS = {
    # 白天背景图
    'day':os.path.join(os.getcwd(),'resources/images/background-day.png'),
    # 晚上背景图
    'night':os.path.join(os.getcwd(),'resources/images/background-night.png')
    }
# 定义管道图片路径
PIPE_IMAGE_PATHS = {

    }