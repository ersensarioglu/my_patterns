import uuid
from uuid_strategy import UuidStrategy

class Uuid1UuidStrategy(UuidStrategy): 
    def generate(self) -> str: 
        return uuid.uuid1()