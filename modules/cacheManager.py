import os
import shutil

def clearCache():
    user_temp_path = os.path.join(
        os.environ["USERPROFILE"], "AppData", "Local", "Temp")
    windows_temp_path = os.path.join("C:\\", "Windows", "Temp")

    try:
        # Удаление данных из папки %temp%
        for filename in os.listdir(user_temp_path):
            file_path = os.path.join(user_temp_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    print(f"Файл {file_path} успешно удален!")
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Ошибка: {file_path}: {e}")

        # Удаление данных из папки temp
        for filename in os.listdir(windows_temp_path):
            file_path = os.path.join(windows_temp_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    print(f"Файл {file_path} успешно удален!")
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Ошибка: {file_path}: {e}")

        print("Кэш данных успешно очищен!")
    except Exception as e:
        print(f"Ошибка: {e}")
