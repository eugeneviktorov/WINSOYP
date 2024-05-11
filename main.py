from tkinter import *
import customtkinter as ctk

# Контент
from content import Content

# Системное окно
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
ctk.set_widget_scaling(1.3)

# Класс для прокрутка окна
class Window(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.content = Content(self)

# Значения окна
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('WINSOYP')
        self.resizable(width=True, height=True)
        self.wm_minsize(720, 580)
        self.my_frame = Window(master=self, width=420, height=340, fg_color="transparent")
        self.my_frame.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # self.iconbitmap('image/icon.ico') // Работает, но не является хорошим решением

        # Центрирование окна
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Вычисление координат для центрирования окна
        x = (screen_width - 420) // 2
        y = (screen_height - 340) // 2
        # Установка позиции окна
        self.geometry(f"{x}+{y}")

root = App()
root.mainloop()
