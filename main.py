from rembg import remove
import easygui
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from image_widgets import *
from sidebar import Sidebar

class App(ctk.CTk):
    def __init__(self):
        #setup
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1000x600')
        self.title('Removedor de Background')
        self.minSize = (800, 500)

        #layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2,uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')

        #widgets
        self.image_import = ImageImport(self, self.import_image)


        #run
        self.mainloop()


    def import_image(self,path):
        self.image = Image.open(path)
        self.image_ratio = self.image.size[0] / self.image.size[1]
        self.image_tk = ImageTk.PhotoImage(self.image)

        self.image_import.grid_forget()
        self.image_output = ImageOutput(self, self.resize_image)
        self.close_button = CloseOutput(self, self.close_edit)
        self.sidebar = Sidebar(self)


    def close_edit(self):
         self.image_output.grid_forget()
         self.close_button.place_forget()
         self.sidebar.grid_forget()
         self.image_import = ImageImport(self, self.import_image)

    def resize_image(self, event):
        canvas_ratio = event.width / event.height

        #resize
        if canvas_ratio > self.image_ratio:
            image_height = int(event.height)
            image_width = int(image_height * self.image_ratio)
        else:
            image_width = int(event.width)
            image_height = int(image_width / self.image_ratio)

        #alocando a imagem
        self.image_output.delete('all')
        resized_image=self.image.resize((image_width, image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image(event.width/2, event.height/2, image = self.image_tk)

App()

#
# window = tk.Tk()
#
# window.title('Removedor de fundo')
# window.geometry('800x600')
# title_label = ttk.Label(master = window, text = 'Removedor de Background', font = 'Calibri 24 bold')
# title_label.pack()
#
# input_frame = ttk.Frame(master = window)
# entry = ttk.Entry(master = input_frame, width = 40)

# button = ttk.Button(master = input_frame, text = 'Remover fundo')
# entry.pack(side = 'left', padx = 10, pady = 10)
# button.pack(side = 'left')
# input_frame.pack(pady = 10, padx = 10)

# inputPath = easygui.fileopenbox(title='Select a file')
# outputPath = easygui.filesavebox(title='Save file to')
#
# input = Image.open(inputPath)
# output = remove(input)
# output.save(outputPath)
# output.save(outputPath)
#
# window.mainloop()