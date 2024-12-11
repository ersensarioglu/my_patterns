import random
import string
from uuid_strategy import UuidStrategy

class SimpleUuidStrategy(UuidStrategy): 
    def generate(self) -> str: 
        return ''.join(random.choices(string.ascii_lowercase, k=30))