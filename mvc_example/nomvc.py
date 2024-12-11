import tkinter as tk
import uuid

class UUIDGen():
    def __init__(self):
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
        self.generate_uuid_button = tk.Button(self.frame, text="Generate", command=self.handle_click_generate_uuid)
        self.generate_uuid_button.pack()
        self.clear_button = tk.Button(self.frame, text="Clear", command=self.handle_click_clear_list)
        self.clear_button.pack()
        
        # initialise the uuid list
        self.uuid = []
        
        # start the main loop
        self.root.mainloop()
        
    def handle_click_generate_uuid(self):
        self.uuid.append(uuid.uuid4())
        self.list.insert(tk.END, self.uuid[-1])
        
    def handle_click_clear_list(self):
        self.uuid = []
        self.list.delete(0, tk.END)

# Start the application
U = UUIDGen()
