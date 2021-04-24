'''
功能描述:
        强化学习模块
作者:
    Fowindy
微信:
    17786508658
github:
       https://github.com/Fowindy/Python_Learning.git
创建时间:
        2020年3月19日 星期四 18:35:32 
'''
import pickle
import random
import numpy as np


'''q learning agent'''
class QLearningAgent():
    def __init__(self, mode, **kwargs):
        self.mode = mode
        # 深度学习_学习率
        self.learning_rate = 0.7
        # 深度学习_贴现因数
        self.discount_factor = 0.95
        # 存储必要的历史数据,格式为:[previous_state, previous_action, state, reward]
        self.history_storage = []
        # 存储强化变量
        self.qvalues_storage = np.zeros((130, 130, 20, 2))
        # 存储每一段的得分
        self.scores_storage = []
        # 之前的状态
        self.previous_state = []
        # 0:不动作, 1:飞翔
        self.previous_action = 0
        # 每一段的数值
        self.num_episode = 0
        # 迄今为此的最大得分
        self.max_score = 0
    '''描述训练行为'''
    def act(self, delta_x, delta_y, bird_speed):
        if not self.previous_state:
            self.previous_state = [delta_x, delta_y, bird_speed]
            return self.previous_action
        if self.mode == 'train':
            state = [delta_x, delta_y, bird_speed]
            self.history_storage.append([self.previous_state, self.previous_action, state, 0])
            self.previous_state = state
        # make a decision according to the qvalues
        if self.qvalues_storage[delta_x, delta_y, bird_speed][0] >= self.qvalues_storage[delta_x, delta_y, bird_speed][1]:
            self.previous_action = 0
        else:
            self.previous_action = 1
        return self.previous_action
    '''设置奖项'''
    def setReward(self, reward):
        if self.history_storage:
            self.history_storage[-1][3] = reward
    '''在后一段更新学习强度变量'''
    def update(self, score, is_logging=True):
        self.num_episode += 1
        self.max_score = max(self.max_score, score)
        self.scores_storage.append(score)
        if is_logging:
            print('Episode: %s, Score: %s, Max Score: %s' % (self.num_episode, score, self.max_score))
        if self.mode == 'train':
            history = list(reversed(self.history_storage))
            # 纠正碰撞前的最后几个错误状态
            num_penalization = 2 
            for item in history:
                previous_state, previous_action, state, reward = item
                if num_penalization > 0:
                    num_penalization -= 1
                    reward = -1000000
                x_0, y_0, z_0 = previous_state
                x_1, y_1, z_1 = state
                self.qvalues_storage[x_0, y_0, z_0, previous_action] = (1 - self.learning_rate) * self.qvalues_storage[x_0, y_0, z_0, previous_action] +\
                                                                       self.learning_rate * (reward + self.discount_factor * max(self.qvalues_storage[x_1, y_1, z_1]))
            self.history_storage = []
    '''保存模型'''
    def saveModel(self, modelpath):
        data = {
                'num_episode': self.num_episode,
                'max_score': self.max_score,
                'scores_storage': self.scores_storage,
                'qvalues_storage': self.qvalues_storage
            }
        with open(modelpath, 'wb') as f:
            pickle.dump(data, f)
        print('[INFO]: save checkpoints in %s...' % modelpath)
    '''load the model'''
    def loadModel(self, modelpath):
        print('[INFO]: load checkpoints from %s...' % modelpath)
        with open(modelpath, 'rb') as f:
            data = pickle.load(f)
        self.num_episode = data.get('num_episode')
        self.qvalues_storage = data.get('qvalues_storage')


'''具有ε-贪婪策略的强化学习代理'''
class QLearningGreedyAgent(QLearningAgent):
    def __init__(self, mode, **kwargs):
        super(QLearningGreedyAgent, self).__init__(mode, **kwargs)
        self.epsilon = 0.1
        self.epsilon_end = 0.0
        self.epsilon_decay = 1e-5
    '''描述训练行为'''
    def act(self, delta_x, delta_y, bird_speed):
        if not self.previous_state:
            self.previous_state = [delta_x, delta_y, bird_speed]
            return self.previous_action
        if self.mode == 'train':
            state = [delta_x, delta_y, bird_speed]
            self.history_storage.append([self.previous_state, self.previous_action, state, 0])
            self.previous_state = state
            # 贪心策略
            if random.random() <= self.epsilon:
                self.previous_action = random.choice([0, 1])
            else:
                if self.qvalues_storage[delta_x, delta_y, bird_speed][0] >= self.qvalues_storage[delta_x, delta_y, bird_speed][1]:
                    self.previous_action = 0
                else:
                    self.previous_action = 1
            return self.previous_action
        else:
            super().act(delta_x, delta_y, bird_speed)
    '''在后一段更新学习强度变量'''
    def update(self, score, is_logging=True):
        self.num_episode += 1
        self.max_score = max(self.max_score, score)
        self.scores_storage.append(score)
        if is_logging:
            print('Episode: %s, Epsilon: %s, Score: %s, Max Score: %s' % (self.num_episode, self.epsilon, score, self.max_score))
        if self.mode == 'train':
            history = list(reversed(self.history_storage))
            # 纠正碰撞前的最后几个错误状态
            num_penalization = 2 
            for item in history:
                previous_state, previous_action, state, reward = item
                if num_penalization > 0:
                    num_penalization -= 1
                    reward = -1000000
                x_0, y_0, z_0 = previous_state
                x_1, y_1, z_1 = state
                self.qvalues_storage[x_0, y_0, z_0, previous_action] = (1 - self.learning_rate) * self.qvalues_storage[x_0, y_0, z_0, previous_action] +\
                                                                       self.learning_rate * (reward + self.discount_factor * max(self.qvalues_storage[x_1, y_1, z_1]))
            self.history_storage = []
            if self.epsilon > self.epsilon_end:
                self.epsilon -= self.epsilon_decay
    '''保存模型'''
    def saveModel(self, modelpath):
        data = {
                'num_episode': self.num_episode,
                'max_score': self.max_score,
                'scores_storage': self.scores_storage,
                'qvalues_storage': self.qvalues_storage,
                'epsilon': self.epsilon
            }
        with open(modelpath, 'wb') as f:
            pickle.dump(data, f)
        print('[INFO]: save checkpoints in %s...' % modelpath)
    '''加载模型'''
    def loadModel(self, modelpath):
        print('[INFO]: load checkpoints from %s...' % modelpath)
        with open(modelpath, 'rb') as f:
            data = pickle.load(f)
        self.num_episode = data.get('num_episode')
        self.qvalues_storage = data.get('qvalues_storage')
        self.epsilon = data.get('epsilon')