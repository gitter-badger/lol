import random

def generate(dist):
    if dist == 'normal':
        return random.gauss(0, 1)
    elif dist == 'uniform':
        return random.random()
