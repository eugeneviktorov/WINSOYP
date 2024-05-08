import os
import shutil

def cacheNVIDIA():
    user_profile = os.environ.get('USERPROFILE')
    glcache_path = os.path.join(
        user_profile, 'AppData', 'Local', 'NVIDIA', 'GLCache')

    try:
        if os.path.exists(glcache_path):
            shutil.rmtree(glcache_path)
            print(f"NVIDIA кэш очищен!")
        else:
            print(f"Директория {glcache_path} не существует.")
    except Exception as e:
        print(f"Ошибка: {glcache_path}: {e}")
