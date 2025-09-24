tk.Label(self.frame_texts,text="OBJETIVOS OBLIGATORIOS", bg="#D3D3D3", font="Verdana 12 bold").grid(row=0, column=0, sticky="ew")
        row_counter += 1
        for i in range(n_oblig):
            tk.Entry(self.frame_texts, width=80).grid(row=row_counter, column=0, pady=2)
            row_counter += 1