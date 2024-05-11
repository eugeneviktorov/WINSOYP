import os

def windowsPrefetch():
    windows_prefetch_path = os.path.join("C:\\", "Windows", "Prefetch")

    try:
        if os.path.exists(windows_prefetch_path):
            for filename in os.listdir(windows_prefetch_path):
                file_path = os.path.join(windows_prefetch_path, filename)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                        print(f"Файл {file_path} успешно удален!")
                except Exception as e:
                    print(f"Ошибка: {file_path}: {e}")
            print("Данных о запускаемых приложениях очищены!")
        else:
            print("Папка не найдена!")
    except Exception as e:
        print(f"Ошибка: {e}")
