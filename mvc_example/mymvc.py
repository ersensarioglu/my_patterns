from mymodel import TkModel
from myview import TkView
from mycontroller import Controller
from uuid4_uuid_strategy import Uuid4UuidStrategy

c = Controller(TkModel(), TkView(), Uuid4UuidStrategy())
c.start()