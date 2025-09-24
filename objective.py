from tkinter import *
import tkinter as tk 
from tkinter import ttk, messagebox

class Objective(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.spn_oblig = None
        self.spn_desea = None
        self.spn_estra = None
        self.frame_texts = None
        self.widgets()
        
    def generateTables(self):
        
        #Elimina todos los elementos
        for w in self.frame_texts.winfo_children():
            w.destroy()

        n_oblig = int(self.spn_oblig.get())
        n_desea = int(self.spn_desea.get())
        n_estra = int(self.spn_estra.get())

        if n_oblig == 0 or n_desea == 0 or n_estra <= 1:
            from tkinter import messagebox
            messagebox.showwarning("Aviso", "Debe haber al menos 1 objetivo obligatorio y deseado, y al menos 2 estrategias")
            return 
        #Aqui pones las tablas o las estrategias mamahuevo
        
        
    def widgets(self):
        
        ancho = self.winfo_screenwidth()
        alto = self.winfo_screenheight()
        
        frame1 = tk.Frame(self, bg="#A5A5A5",highlightbackground="gray",highlightthickness= 1)
        frame1.place(x=0,y=0,width=ancho,height=alto)
        
        titulo = tk.Label(self,text="OBJETIVOS OBLIGATORIOS Y DESEADOS",bg="#24508A",font="Verdana 30 bold",anchor="center")
        titulo.place(x=5,y=5,width=ancho - 10,height=90)
        
        contenedor = tk.Frame(frame1, bg="#A5A5A5")
        contenedor.place(relx=0.5, y=150,anchor="center")
        
        tk.Label(contenedor, text="Ingrese # de objetivos obligatorios", bg="#A5A5A5", font="Verdana 14").grid(row=0, column=0, padx=20, pady=5)
        self.spn_oblig = tk.Spinbox(contenedor, from_=0, to=50, width=5, font="Verdana 12")
        self.spn_oblig.grid(row=1, column=0, padx=20, pady=5)

        tk.Label(contenedor, text="Ingrese # de objetivos deseados", bg="#A5A5A5", font="Verdana 14").grid(row=0, column=1, padx=20, pady=5)
        self.spn_desea = tk.Spinbox(contenedor, from_=0, to=50, width=5, font="Verdana 12")
        self.spn_desea.grid(row=1, column=1, padx=20, pady=5)

        tk.Label(contenedor, text="Ingrese el # de estrategias", bg="#A5A5A5", font="Verdana 14").grid(row=0, column=2, padx=20, pady=5)
        self.spn_estra = tk.Spinbox(contenedor, from_=0, to=50, width=5, font="Verdana 12")
        self.spn_estra.grid(row=1, column=2, padx=20, pady=5)
        
        btnGenerator = tk.Button(
            contenedor,
            text="GENERAR",
            bg="#ffffff",
            fg="#24508A",
            font="Verdana 14 bold",
            anchor="center",
            command=self.generateTables
        )       
        btnGenerator.grid(row=1, column=3, padx=40, pady=10)
        
        canvas = tk.Canvas(frame1, bg="#D3D3D3", width=ancho-40, height=alto-330)
        canvas.place(relx=0.5, y=200, anchor="n")

        scrollbar = tk.Scrollbar(frame1, orient="vertical", command=canvas.yview)
        scrollbar.place(relx=0.98, y=203, height=alto-350, anchor="n")

        canvas.configure(yscrollcommand=scrollbar.set)
        self.frame_texts = tk.Frame(canvas, bg="#D3D3D3")
        canvas.create_window((0,0), window=self.frame_texts, anchor="nw")

        self.frame_texts.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))