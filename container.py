from tkinter import *
import tkinter as tk 
from objective import Objective
from tkinter import messagebox
from PIL import Image, ImageTk

class Container(tk.Frame):
    def __init__(self, father, controller):
        super().__init__(father)
        self.controller = controller
        self.place(x=0,y=0,width=800,height=550)
        self.config(bg="#24508A")
        
        self.logo_image2 = ImageTk.PhotoImage(
            Image.open("iconos/LOGO_SIS.png").resize((120, 100),Image.LANCZOS)
        )
        self.logo_label2 = tk.Label(self, image=self.logo_image2, bg="#24508A")
        self.logo_label2.place(x=665, y=5)
        
        self.titulo = tk.Label(
            self,
            text="DeciCASE",
            bg="#24508A",
            fg="white",
            font=("Verdana", 60, "bold"),
            anchor="center"
        )
        self.titulo.place(x=140, y=5, width=525, height=100)
        
        self.widgets()
    
    def show_frames(self, container):
        top_level = tk.Toplevel(self)
        frame = container(top_level)
        frame.config(bg="#24508A")
        frame.pack(fill="both",expand=True)
        ancho = self.winfo_screenwidth()
        alto = self.winfo_screenheight()
        top_level.geometry(f"{ancho}x{alto}+0+0")
        top_level.resizable(False,False)
        
    def dataWindow(self):
        self.show_frames(Objective)
        
    def exitWindow(self):
        respuesta = messagebox.askyesno("Salir", "¿Desea salir de la aplicación?")
        if respuesta:
            self.controller.destroy() 
        
    def widgets(self):
        
        frame1 = tk.Frame(self, bg="#8297B2")
        frame1.place(x=0,y=115,width=800,height=500)
        
        btnObjective = Button(frame1, bg="#ffffff",fg="#24508A",font="Verdana 20 bold",text="EMPEZAR",command=self.dataWindow)
        btnObjective.place(x=492.5,y=93,width=240,height=60)
        
        btnExit = Button(frame1, bg="#ffffff",fg="#24508A",font="Verdana 20 bold",text="SALIR",command=self.exitWindow)
        btnExit.place(x=492.5,y=240,width=240,height=60)
        
        self.logo_image1 = ImageTk.PhotoImage(
            Image.open("iconos/LOGO.png").resize((420, 420),Image.LANCZOS)
        )
        self.logo_label1 = tk.Label(self, image=self.logo_image1, bg="#8297B2")
        self.logo_label1.place(x=5, y=120)
        
        
        