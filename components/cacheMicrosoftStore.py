import subprocess

def cacheMicrosoftStore():
    try:
        subprocess.run(["wsreset.exe"], check=True)
        print("Кэш Microsoft Store успешно очищен!")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка: {e}")
