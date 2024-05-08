import subprocess

def cacheDNS():
    try:
        subprocess.run(["ipconfig", "/flushdns"], check=True)
        print("DNS кэш успешно очищен!")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка: {e}")
