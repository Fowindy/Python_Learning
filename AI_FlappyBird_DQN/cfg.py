# 配置文件
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
                    # 定义蓝色小鸟
                    'blue':{
                        'up':os.path.join(os.getcwd(),'resources/images/bluebird-upflap.png'),
                        'mid':os.path.join(os.getcwd(),'resources/images/bluebird-midflap.png'),
                        'down':os.path.join(os.getcwd(),'resources/images/bluebird-downflap.png')
                        },
                    }