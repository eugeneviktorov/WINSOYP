import os

def windowsDownload():
    windows_download_path = os.path.join(
        "C:\\", "Windows", "SoftwareDistribution", "Download")

    try:
        if os.path.exists(windows_download_path):
            for filename in os.listdir(windows_download_path):
                file_path = os.path.join(windows_download_path, filename)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                        print(f"Файл {file_path} успешно удален!")
                except Exception as e:
                    print(f"Ошибка: {file_path}: {e}")
            print("Файлы обновления windows удалены!")
        else:
            print("Папка не найдена!")
    except Exception as e:
        print(f"Ошибка: {e}")
