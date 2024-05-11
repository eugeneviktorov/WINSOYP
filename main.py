from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import webbrowser

# Глобальные компонентные модели
from modules.params import globalColors, globalFont

# Очистка сестемы
from components.cacheManager import clearCache
from components.cacheDNS import cacheDNS
from components.cacheNVIDIA import cacheNVIDIA
from components.cacheMicrosoftStore import cacheMicrosoftStore
from components.windowsDownload import windowsDownload
from components.windowsPrefetch import windowsPrefetch
from components.systemRestorePoints import deleteSystemRestorePoints
from components.openCleanmgr import openCleanmgr



# Системное окно
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
ctk.set_widget_scaling(1.2)



# Класс для прокрутка окна
class MyFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Название программы
        self.labelName = ctk.CTkLabel(self, text="Windows System Optimization", font=(globalFont, 18))
        self.labelName.pack(pady=(20, 0))

        # Автор программы
        labelAuthor = ctk.CTkLabel(self, text="By @eugeneviktorov", font=(globalFont, 14))
        labelAuthor.pack(pady=(0, 0))

        # Открытие ссылки в браузере
        def openLink(event):
            webbrowser.open("https://viktorovvv.ru")

        # Ссылка на сайт автора
        labelLink = ctk.CTkLabel(self, text="viktorovvv.ru", text_color=globalColors['link'] , font=(globalFont, 14), cursor="hand2")
        labelLink.pack(pady=(0, 20))
        labelLink.bind("<Button-1>", openLink)



        # Функция для очистки и подтверждения
        def clearAndConfirm():
            if not cacheChecked.get() and not cacheNVIDIAChecked.get() and not cacheDNSChecked.get() and not storeChecked.get() and not downloadChecked.get() and not prefetchChecked.get() and not pointsChecked.get():
                messagebox.showerror("Ошибка", "Не выбран ни один пункт очистки!")
            else:
                clearAndConfirm = messagebox.askquestion("Подтверждение", "Вы уверены что хотите сделать очистку файлов?")
                if clearAndConfirm == 'yes':
                    if cacheChecked.get():
                        clearCache()
                    if cacheNVIDIAChecked.get():
                        cacheNVIDIA()
                    if cacheDNSChecked.get():
                        cacheDNS()
                    if storeChecked.get():
                        cacheMicrosoftStore()
                    if downloadChecked.get():
                        windowsDownload()
                    if prefetchChecked.get():
                        windowsPrefetch()
                    if pointsChecked.get():
                        deleteSystemRestorePoints()
                    messagebox.showinfo(title="Информация", message="Файлы удалены!")

        # Функция отметок
        def createCheckbox(self, text, variable):
            checkbox = ctk.CTkCheckBox(self, text=text, variable=variable, hover=False,)
            checkbox.pack(pady=5, padx=5, anchor='w')

        # Переменные для флажков
        cacheChecked = ctk.BooleanVar()
        cacheNVIDIAChecked = ctk.BooleanVar()
        cacheDNSChecked = ctk.BooleanVar()
        storeChecked = ctk.BooleanVar()
        downloadChecked = ctk.BooleanVar()
        prefetchChecked = ctk.BooleanVar()
        pointsChecked = ctk.BooleanVar()

        # Создаем флажки с помощью функции
        createCheckbox(self, "Кэш системы", cacheChecked, )
        createCheckbox(self, "Кэш NVIDIA", cacheNVIDIAChecked, )
        createCheckbox(self, "Кэш DNS", cacheDNSChecked, )
        createCheckbox(self, "Кэш Microsoft Store", storeChecked, )
        createCheckbox(self, "Файлы обновления Windows", downloadChecked, )
        createCheckbox(self, "Данные о запускаемых программах", prefetchChecked, )
        createCheckbox(self, "Точки восстановления (опытным пользователям)", pointsChecked,)

        # Создаем кнопку для подтверждения очистки
        clearButton = ctk.CTkButton(self, text="Очистить", command=clearAndConfirm)
        clearButton.pack(pady=5, padx=5, anchor='w')



        # Описание действия
        openCleanmgrLabel = ctk.CTkLabel(self, text='В данном пункте вам откроется системная программа "Очистка диска". Выбираем диск, отмечаем все пункты и нажимаем на "Очистить системные файлы", также выбираем диск и отмечаем все пункты и нажимаем "Ок".', text_color=globalColors['titleInstruction'], font=(globalFont, 14), wraplength=420, justify='left')
        openCleanmgrLabel.pack(pady=(30, 5), padx=5, anchor='w')

        # Открытие программы "Очистка диска"
        def openAskProgram():
            openAskProgram = messagebox.askquestion("Подтверждение", 'Вы уверены, что хотите открыть программу "Очистка диска?"')
            if openAskProgram == 'yes':
                openCleanmgr()
                print("Открытие программы")

        # Программа "Очистка диска"
        openCleanmgrButton = ctk.CTkButton(self, text='Открыть "Очистка диска"', command=openAskProgram)
        openCleanmgrButton.pack(pady=(0, 20), padx=5, anchor='w')



# Значения окна
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('WINSOYP')
        self.resizable(width=False, height=False)
        self.my_frame = MyFrame(master=self, width=420, height=300, fg_color="transparent")
        self.my_frame.grid(row=0, column=0)
        # self.iconbitmap('logo.ico')

root = App()
root.mainloop()
