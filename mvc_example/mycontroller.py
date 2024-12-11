from mymodel import Model
from myview import View

class Controller:
    def __init__(self, model: Model, view: View, uuid_strategy=None):
        self.model = model
        self.view = view
        self.uuid_strategy = uuid_strategy

    def set_name(self, name):
        self.model.set_name(name)

    def get_name(self):
        return self.model.get_name()

    def start(self):
        self.view.setup(self)
        self.view.start_main_loop()
        
    def set_uuid_strategy(self, uuid_strategy):
        self.uuid_strategy = uuid_strategy
        
    def handle_click_generate_uuid(self):
        self.model.generate_uuid(self.uuid_strategy)
        self.view.append_to_list(self.model.get_uuid())
        
    def handle_click_clear_list(self):
        self.view.clear_list()