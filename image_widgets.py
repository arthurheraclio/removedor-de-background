import customtkinter as ctk
from tkinter import filedialog, Canvas
from config import *



class ImageImport(ctk.CTkFrame):
    def __init__(self,parent, import_function):
        super().__init__(master = parent)
        self.grid(column=0, columnspan=2, row=0, sticky="nsew")
        self.import_function = import_function

        ctk.CTkButton(self, text = 'Escolher imagem', command= self.open_dialog).pack(expand=True)

    def open_dialog(self):
        path = filedialog.askopenfile().name
        self.import_function(path)


class ImageOutput(Canvas):
    def __init__(self,parent, resize_image):
        super().__init__(master = parent, background=BACKGROUND, bd = 0, highlightthickness=0, relief="ridge")
        self.grid(row=0, column=1, sticky="nsew")
        self.bind('<Configure>', resize_image)

class CloseOutput(ctk.CTkButton):
    def __init__(self,parent, close_function):
        super().__init__(master = parent,
                         command= close_function,
                         text = 'x',
                         text_color= WHITE, fg_color='transparent',
                         width = 40, height = 40,
                         hover_color= CLOSE_RED)
        self.place(relx=0.99,rely=0.01, anchor = 'ne')

