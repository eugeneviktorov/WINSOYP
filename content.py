from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from customtkinter import CTkImage, CTkLabel
from PIL import Image
import webbrowser

# Глобальные стили
from styles.globalStyles import globalColors, globalFont

# Очистка системы
from modules.cacheManager import clearCache
from modules.cacheDNS import cacheDNS
from modules.cacheNVIDIA import cacheNVIDIA
from modules.cacheMicrosoftStore import cacheMicrosoftStore
from modules.windowsDownload import windowsDownload
from modules.windowsPrefetch import windowsPrefetch
from modules.systemRestorePoints import deleteSystemRestorePoints
from modules.openCleanmgr import openCleanmgr

class Content:
    def __init__(self, master):
        # Иконка программы
        # icon = CTkImage(light_image=Image.open("image/icon.png"), size=(40, 40))
        # labelImage = CTkLabel(master, image=icon, text='')
        # labelImage.pack(pady=(10, 0))

        # Название программы
        labelName = ctk.CTkLabel(master, text="WINSOYP", font=(globalFont, 18))
        labelName.pack(pady=(10, 0))

        # Открытие ссылки в браузере
        def openLink(event):
            webbrowser.open("https://viktorovvv.ru")

        # Ссылка на сайт автора
        labelLink = ctk.CTkLabel(master, text="viktorovvv.ru", text_color=globalColors['blue'], font=(globalFont, 14), cursor="hand2")
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
                    messagebox.showinfo(title="Информация", message="Очистка прошла успешно!")

        # Функция отметок
        def createCheckbox(master, text, variable):
            checkbox = ctk.CTkCheckBox(master, text=text, variable=variable, hover=False, border_color=globalColors["gray"], fg_color=globalColors["blue"])
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
        createCheckbox(master, "Кэш системы", cacheChecked, )
        createCheckbox(master, "Кэш NVIDIA", cacheNVIDIAChecked, )
        createCheckbox(master, "Кэш DNS", cacheDNSChecked, )
        createCheckbox(master, "Кэш Microsoft Store", storeChecked, )
        createCheckbox(master, "Файлы обновления Windows", downloadChecked, )
        createCheckbox(master, "Данные о запускаемых программах", prefetchChecked, )
        createCheckbox(master, "Точки восстановления (опытным пользователям)", pointsChecked,)

        # Создаем кнопку для подтверждения очистки
        clearButton = ctk.CTkButton(master, text="Очистить", command=clearAndConfirm, fg_color=globalColors["blue"], hover_color=globalColors["darkBlue"], text_color=globalColors["black"])
        clearButton.pack(pady=5, padx=5, anchor='w')

        # Описание действия
        openCleanmgrLabel = ctk.CTkLabel(master, text='В данном пункте откроется встроенная в систему программа "Очистка диска". Выбираем диск, отмечаем все пункты и нажимаем на "Очистить системные файлы", также выбираем диск и отмечаем все пункты и нажимаем "Ок".', font=(globalFont, 14), wraplength=420, justify='left')
        openCleanmgrLabel.pack(pady=(30, 5), padx=5, anchor='w')

        # Открытие программы "Очистка диска"
        def openAskProgram():
            openAskProgram = messagebox.askquestion("Подтверждение", 'Вы уверены, что хотите открыть программу "Очистка диска?"')
            if openAskProgram == 'yes':
                openCleanmgr()
                print("Открытие программы")

        # Программа "Очистка диска"
        openCleanmgrButton = ctk.CTkButton(master, text='Открыть "Очистка диска"', command=openAskProgram, fg_color=globalColors["blue"], hover_color=globalColors["darkBlue"], text_color=globalColors["black"])
        openCleanmgrButton.pack(pady=(0, 20), padx=5, anchor='w')
