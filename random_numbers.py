import random
import uuid

def generate(dist, location, scale):
    if dist == 'normal':
        return random.gauss(location, scale)
    elif dist == 'uniform':
        return random.uniform(location, scale)
    elif dist == 'lognormal':
        return random.lognormvariate(location, scale)
    elif dist == 'int':
        return random.randint(location, scale)
    elif dist == 'uuid':
        return str(uuid.uuid4())
