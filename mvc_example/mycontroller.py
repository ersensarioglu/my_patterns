from mymodel import Model
from myview import View

class Controller:
    def __init__(self, model: Model, view: View, generate_uuid_func):
        self.model = model
        self.view = view
        self.generate_uuid_func = generate_uuid_func

    def set_name(self, name):
        self.model.set_name(name)

    def get_name(self):
        return self.model.get_name()

    def start(self):
        self.view.setup(self)
        self.view.start_main_loop()
        
    def handle_click_generate_uuid(self):
        self.model.generate_uuid(self.generate_uuid_func)
        self.view.append_to_list(self.model.get_uuid())
        
    def handle_click_clear_list(self):
        self.view.clear_list()