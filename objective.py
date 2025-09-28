from tkinter import *
import tkinter as tk 
from tkinter import ttk, messagebox

class Objective(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.spn_oblig = None
        self.spn_desea = None
        self.spn_estra = None
        self.tree = None
        
        self.widgets()
        
    def confirm_generate(self):
        respuesta = messagebox.askyesno("Confirmar", "¿Los datos ingresados son correctos?")
        if respuesta: 
            self.generateTables()
            self.btnGenerator.config(state="disabled")
        
    def generateTables(self):

        if self.tree:
            self.tree.destroy()
        
        try:
            n_oblig = int(self.spn_oblig.get())
            n_desea = int(self.spn_desea.get())
            n_estra = int(self.spn_estra.get())
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar solo números enteros.")
            return  

        if n_oblig == 0 or n_desea == 0 or n_estra <= 1:
            messagebox.showwarning(
            "Aviso",
            "Debe haber al menos 1 objetivo obligatorio y deseado, y al menos 2 estrategias"
            )
            return
        
        # Crear Treeview
        self.tree = ttk.Treeview(self.frame_texts, columns=("Tipo", "Descripción", "Peso"), show="headings")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Peso", text="Peso (0-10)")
        self.tree.column("Tipo", width=150, anchor="center")
        self.tree.column("Descripción", width=500)
        self.tree.column("Peso", width=100, anchor="center")
        
        # Scrollbar vertical
        vsb = ttk.Scrollbar(self.frame_texts, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")
        
        self.tree.tag_configure('obligatorio', background="#F28C8C")  # rojo suave
        self.tree.tag_configure('deseado', background="#8CF2A2")      # verde suave
        self.tree.tag_configure('estrategia', background="#8CC8F2") 
        
        # Insertar filas con tags y valores completos
        for i in range(n_oblig):
            self.tree.insert('', 'end', values=(f"Objetivo obligatorio {i+1}", f"", ""), tags=('obligatorio',))

        for i in range(n_desea):
            self.tree.insert('', 'end', values=(f"Objetivo deseado {i+1}", f"", ""), tags=('deseado',))

        for i in range(n_estra):
            self.tree.insert('', 'end', values=(f"Estrategia {i+1}", f"", ""), tags=('estrategia',))

        # Hacer editable
        self.tree.bind("<Double-1>", self.on_double_click)
        
    def on_double_click(self, event):
        item_id = self.tree.focus()
        col = self.tree.identify_column(event.x)
        if col not in ("#2", "#3"):  
            return
        
        x, y, width, height = self.tree.bbox(item_id, col)
        if not width or not height:
            return
        
        vals = list(self.tree.item(item_id, "values"))
        value = vals[1] if col == "#2" else vals[2]

        entry = Entry(self.tree)
        entry.place(x=x, y=y, width=width, height=height)
        entry.insert(0, value)
        entry.focus()

        def save_edit(event=None):
            vals = list(self.tree.item(item_id, "values"))
            new_val = entry.get()
            vals[1 if col == "#2" else 2] = new_val
            self.tree.item(item_id, values=vals)
            entry.destroy()

        entry.bind("<Return>", save_edit)
        entry.bind("<FocusOut>", save_edit)
        
    def save_data(self):
        obligatorios = []
        deseados = []
        estrategias = []

        for item in self.tree.get_children():
            tipo, desc, peso = self.tree.item(item, "values")


            if not desc.strip():
                messagebox.showerror("Error", f"Falta la descripción en '{tipo}'")
                return

            try:
                peso_val = float(peso)
                if not (0 <= peso_val <= 10):
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", f"Peso inválido en '{tipo}': debe ser un número entre 0 y 10")
                return

            # Guardar en la lista correspondiente
            if tipo.startswith("Obligatorio"):
                obligatorios.append((desc, peso_val))
            elif tipo.startswith("Deseado"):
                deseados.append((desc, peso_val))
            elif tipo.startswith("Estrategia"):
                estrategias.append((desc, peso_val))

        # Mostrar resultados en consola
        print("Obligatorios:", obligatorios)
        print("Deseados:", deseados)
        print("Estrategias:", estrategias)
        messagebox.showinfo("Datos guardados", "Se han capturado los objetivos y estrategias.")
    
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
        
        self.btnGenerator = tk.Button(
            contenedor,
            text="GENERAR",
            bg="#ffffff",
            fg="#24508A",
            font="Verdana 14 bold",
            anchor="center",
            command=self.confirm_generate
        )       
        self.btnGenerator.grid(row=1, column=3, padx=40, pady=10)
        
        self.frame_texts = Frame(frame1, bg="#f0f0f0")
        self.frame_texts.place(relx=0.5, rely=0.55, anchor="center", relwidth=0.9, relheight=0.55)
        
        # Dentro de widgets()
        self.frame_texts_container = Frame(frame1, bg="#f0f0f0")
        self.frame_texts_container.place(relx=0.5, rely=0.55, anchor="center", relwidth=0.9, relheight=0.60)

        # Botón guardar fijo al final
        self.save_btn = Button(self.frame_texts_container, text="GUARDAR", fg="#24508A", bg="#f0f0f0",
                       font="Verdana 14 bold", command=self.save_data)
        self.save_btn.pack(side="bottom", pady=10)

        # Frame para el Treeview
        self.frame_texts = Frame(self.frame_texts_container, bg="#f0f0f0")
        self.frame_texts.pack(fill="both", expand=True)