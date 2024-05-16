import random
from faker import Faker

class BaseFixture:
    def __init__(self):
        self.faker = Faker()
    
    def GetRandomBoolean(self):
        return bool(random.randint(0, 1))