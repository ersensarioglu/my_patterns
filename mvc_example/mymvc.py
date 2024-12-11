from mymodel import TkModel
from myview import TkView
from mycontroller import Controller
from uuid4_uuid_strategy import Uuid4UuidStrategy

c = Controller(TkModel(), TkView())
c.set_uuid_strategy(Uuid4UuidStrategy())
# Above two lines are equivalent to:
# c = Controller(TkModel(), TkView(), Uuid4UuidStrategy())
# But if there are so many different strategies to add, 
# it is better to set the strategy separately.
c.start()