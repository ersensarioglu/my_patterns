import uuid
from uuid_strategy import UuidStrategy

class Uuid4UuidStrategy(UuidStrategy): 
    def generate(self) -> str: 
        return uuid.uuid4()