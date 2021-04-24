'''
功能描述:
        使用Deep Q Network强化学习算法智能玩飞翔的小鸟
作者:
    Fowindy
微信:
    17786508658
github:
       https://github.com/Fowindy/Python_Learning.git
创建时间:
        2020年03月19日 13:30:25   
'''
import os #导入os模块：负责程序和操作系统之间的交互
import cfg #导入cfg配置文件模块：用于调用游戏参数以及资源
import sys # 导入sys模块:用于操控python的运行时环境
import random # 导入random模块:用于生成游戏中的随机变量
import pygame # 导入pygame模块:用于设计游戏界面
import argparse # 导入argparse模块:用于解析命令行参数
from modules.sprites.Pipe import * # 导入本地精灵类Pipe模块
from modules.sprites.Bird import * ##导入Bird资源:面向对象的思维_自定义封装鸟类模块
from modules.interfaces.endGame import * ##导入endGame接口:面向对象的思维_自定义封装结束游戏接口
from modules.interfaces.startGame import * ##导入startGame接口:面向对象的思维_自定义封装开始游戏接口
from modules.QLearningAgent.QLearningAgent import * ##导入QLearningAgent代理:面向对象的思维_导入强化学习算法代理


'''分析参数'''
def parseArgs():
	parser = argparse.ArgumentParser(description='Use q learning to play flappybird')
	parser.add_argument('--mode', dest='mode', help='Choose <train> or <test> please', default='train', type=str)
	parser.add_argument('--policy', dest='policy', help='Choose <plain> or <greedy> please', default='plain', type=str)
	args = parser.parse_args()
	return args


'''初始化游戏'''
def initGame():
	pygame.init()
	pygame.mixer.init()
	screen = pygame.display.set_mode((cfg.SCREENWIDTH, cfg.SCREENHEIGHT))
	pygame.display.set_caption('AI_Bird-作者:Fowindy')
	return screen


'''显示游戏得分'''
def showScore(screen, score, number_images):
	digits = list(str(int(score)))
	width = 0
	for d in digits:
		width += number_images.get(d).get_width()
	offset = (cfg.SCREENWIDTH - width) / 2
	for d in digits:
		screen.blit(number_images.get(d), (offset, cfg.SCREENHEIGHT*0.1))
		offset += number_images.get(d).get_width()


'''调用主函数'''
def main(mode, policy, agent, modelpath):
	screen = initGame()
	# 加载必要游戏资源
	# 加载必要声音资源
	sounds = dict()
	for key, value in cfg.AUDIO_PATHS.items():
		sounds[key] = pygame.mixer.Sound(value)
	# 加载分数图片
	number_images = dict()
	for key, value in cfg.NUMBER_IMAGE_PATHS.items():
		number_images[key] = pygame.image.load(value).convert_alpha()
	# 加载管道图片
	pipe_images = dict()
	pipe_images['bottom'] = pygame.image.load(random.choice(list(cfg.PIPE_IMAGE_PATHS.values()))).convert_alpha()
	pipe_images['top'] = pygame.transform.rotate(pipe_images['bottom'], 180)
	# 加载小鸟图片
	bird_images = dict()
	for key, value in cfg.BIRD_IMAGE_PATHS[random.choice(list(cfg.BIRD_IMAGE_PATHS.keys()))].items():
		bird_images[key] = pygame.image.load(value).convert_alpha()
	# 加载背景图片
	backgroud_image = pygame.image.load(random.choice(list(cfg.BACKGROUND_IMAGE_PATHS.values()))).convert_alpha()
	# 加载其它图片
	other_images = dict()
	for key, value in cfg.OTHER_IMAGE_PATHS.items():
		other_images[key] = pygame.image.load(value).convert_alpha()
	# 调用开始游戏接口
	game_start_info = startGame(screen, sounds, bird_images, other_images, backgroud_image, cfg, mode)
	# 进入游戏主流程
	score = 0
	bird_pos, base_pos, bird_idx = list(game_start_info.values())
	base_diff_bg = other_images['base'].get_width() - backgroud_image.get_width()
	clock = pygame.time.Clock()
	# 实例化管道对象
	pipe_sprites = pygame.sprite.Group()
	for i in range(2):
		pipe_pos = Pipe.randomPipe(cfg, pipe_images.get('top'))
		pipe_sprites.add(Pipe(image=pipe_images.get('top'), position=(cfg.SCREENWIDTH+200+i*cfg.SCREENWIDTH/2, pipe_pos.get('top')[-1]), type_='top'))
		pipe_sprites.add(Pipe(image=pipe_images.get('bottom'), position=(cfg.SCREENWIDTH+200+i*cfg.SCREENWIDTH/2, pipe_pos.get('bottom')[-1]), type_='bottom'))
	# 实例化小鸟对象
	bird = Bird(images=bird_images, idx=bird_idx, position=bird_pos)
	# 判断是否增加管道
	is_add_pipe = True
	# 判断游戏是否继续或结束
	is_game_running = True
	while is_game_running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				if mode == 'train': agent.saveModel(modelpath)
				pygame.quit()
				sys.exit()
		# 调用深度学习模型开始控制小鸟动作
		delta_x = 10000
		delta_y = 10000
		for pipe in pipe_sprites:
			if pipe.type_ == 'bottom' and (pipe.rect.left-bird.rect.left+30) > 0:
				if pipe.rect.right - bird.rect.left < delta_x:
					delta_x = pipe.rect.left - bird.rect.left
					delta_y = pipe.rect.top - bird.rect.top
		delta_x = int((delta_x + 60) / 5)
		delta_y = int((delta_y + 225) / 5)
		if agent.act(delta_x, delta_y, int(bird.speed+9)):
			bird.setFlapped()
			sounds['wing'].play()
		# 检查小鸟是否与管道相撞
		for pipe in pipe_sprites:
			if pygame.sprite.collide_mask(bird, pipe):
				sounds['hit'].play()
				is_game_running = False
		# 刷新小鸟状态
		boundary_values = [0, base_pos[-1]]
		is_dead = bird.update(boundary_values)
		if is_dead:
			sounds['hit'].play()
			is_game_running = False
		# 如果游戏结束存储强化学习变量
		if not is_game_running:
			agent.update(score, True) if mode == 'train' else agent.update(score, False)
		# 左移基座，达到鸟前飞的效果
		base_pos[0] = -((-base_pos[0] + 4) % base_diff_bg)
		# 将管子向左移动，达到鸟前飞的效果
		flag = False
		reward = 1
		for pipe in pipe_sprites:
			pipe.rect.left -= 4
			if pipe.rect.centerx <= bird.rect.centerx and not pipe.used_for_score:
				pipe.used_for_score = True
				score += 0.5
				reward = 5
				if '.5' in str(score):
					sounds['point'].play()
			if pipe.rect.left < 5 and pipe.rect.left > 0 and is_add_pipe:
				pipe_pos = Pipe.randomPipe(cfg, pipe_images.get('top'))
				pipe_sprites.add(Pipe(image=pipe_images.get('top'), position=pipe_pos.get('top'), type_='top'))
				pipe_sprites.add(Pipe(image=pipe_images.get('bottom'), position=pipe_pos.get('bottom'), type_='bottom'))
				is_add_pipe = False
			elif pipe.rect.right < 0:
				pipe_sprites.remove(pipe)
				flag = True
		if flag: is_add_pipe = True
		# 设置奖项
		if mode == 'train' and is_game_running: agent.setReward(reward)
		# 在屏幕上显示必要的游戏元素
		screen.blit(backgroud_image, (0, 0))
		pipe_sprites.draw(screen)
		screen.blit(other_images['base'], base_pos)
		showScore(screen, score, number_images)
		bird.draw(screen)
		pygame.display.update()
		clock.tick(cfg.FPS)
	# 调用游戏结束的接口
	endGame(screen, sounds, showScore, score, number_images, bird, pipe_sprites, backgroud_image, other_images, base_pos, cfg, mode)


'''run'''
if __name__ == '__main__':
	# parse arguments in command line
	args = parseArgs()
	mode = args.mode.lower()
	policy = args.policy.lower()
	assert mode in ['train', 'test'], '--mode should be <train> or <test>'
	assert policy in ['plain', 'greedy'], '--policy should be <plain> or <greedy>'
	# the instanced class of QLearningAgent or QLearningGreedyAgent, and the path to save and load model
	if not os.path.exists('checkpoints'):
		os.mkdir('checkpoints')
	agent = QLearningAgent(mode) if policy == 'plain' else QLearningGreedyAgent(mode)
	modelpath = 'checkpoints/qlearning_%s.pkl' % policy
	if os.path.isfile(modelpath):
		agent.loadModel(modelpath)
	# begin game
	while True:
		main(mode, policy, agent, modelpath)