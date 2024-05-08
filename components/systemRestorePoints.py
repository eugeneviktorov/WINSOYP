import subprocess

def deleteSystemRestorePoints():
    try:
        subprocess.run(["vssadmin", "delete", "shadows", "/all", "/quiet"], check=True)
        print("Точки восстановления удалены!")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка: {e}")
