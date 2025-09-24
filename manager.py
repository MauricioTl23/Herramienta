from tkinter import *
import tkinter as tk
from container import Container

class Manager(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.title("DeciCASE v1.0")
        self.resizable(False,False)
        self.configure(bg="#24508A")
        self.center_window(800,600)
        
        self.container = Frame(self,bg="#24508A")
        self.container.pack(fill = "both",expand=True)
        
        titulo = tk.Label(self,text="© 2025 Universidad Técnica de Oruro - Ingeniería de Sistemas",bg="#24508A",font="Verdana 10",anchor="center")
        titulo.place(x=5,y=555,width=790,height=40)
        
        self.frames = {
            Container: None
        }
        
        self.load_frames()
        self.show_frames(Container)
        
    def load_frames(self):
        for FrameClass in self.frames.keys():
            frame = FrameClass(self.container,self)
            self.frames[FrameClass] = frame
            
    def show_frames(self,frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()
        
    def center_window(self, width=800, height=600):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
    
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
    
        self.geometry(f"{width}x{height}+{x}+{y}")
        
def main():
    app = Manager()
    app.mainloop()
    
if __name__ == "__main__":
    main()
        