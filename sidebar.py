import customtkinter as ctk
import tkinter as tk

class Sidebar(ctk.CTkTabview):
    def __init__(self, parent):
        super().__init__(master =parent)
        self.grid(row=0,column=0, sticky="nsew")

        self.add('Remover fundo')
        self.add('Exportar')