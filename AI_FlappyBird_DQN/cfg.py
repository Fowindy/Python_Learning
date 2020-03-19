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