import subprocess

def openCleanmgr():
    try:
        subprocess.Popen(["cleanmgr.exe"])
    except Exception as e:
        print(f"Ошибка: {e}")
