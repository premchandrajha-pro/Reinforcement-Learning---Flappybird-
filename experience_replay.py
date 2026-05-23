# creating experince replay for solving the problem of collinearity 

from collections import deque
# seque is teh python datastructre which uses FIFO topology
import random


class ReplayMemory():
    #create FIFO queue = experience replay
    def __init__(self, maxlen, seed=None):  # max length = maxlen = size of replay memory
        self.memory = deque([], maxlen = maxlen)  # created the datastructure


    def append(self, new_experience):
        self.memory.append(new_experience)

    def sample(self, sample_size):
        return random.sample(self.memory, sample_size)
        # this function is for taking out random sample from experience memory of gven sample size
        
    def __len__(self): # private function __{private function name}__
        return len(self.memory)