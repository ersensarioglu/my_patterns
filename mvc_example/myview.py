import tkinter as tk

from abc import ABC, abstractmethod

class View(ABC):
    @abstractmethod
    def setup(self, controller):
        pass
    
    @abstractmethod
    def append_to_list(self, item):
        pass
    
    @abstractmethod
    def clear_list(self):
        pass
    
    @abstractmethod
    def start_main_loop(self):
        pass

class TkView(View):
    def setup(self, controller):
        # setup tkinter
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("UUID Generator")
        
        # create the gui
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.label = tk.Label(self.frame, text="UUID Generator")
        self.label.pack()
        self.list = tk.Listbox(self.frame)
        self.list.pack(fill=tk.BOTH, expand=True)
        self.generate_uuid_button = tk.Button(self.frame, text="Generate", command=controller.handle_click_generate_uuid)
        self.generate_uuid_button.pack()
        self.clear_button = tk.Button(self.frame, text="Clear", command=controller.handle_click_clear_list)
        self.clear_button.pack()
        
    def append_to_list(self, item):
        self.list.insert(tk.END, item)
        
    def clear_list(self):
        self.list.delete(0, tk.END)
        
    def start_main_loop(self):
        self.root.mainloop()
        