import os
from dotenv import load_dotenv

# Загружаем переменные из .env (если файл есть)
load_dotenv()

def print_author():
    # Читаем значение из переменной окружения AUTHOR
    author = os.getenv("AUTHOR")
    
    # Если AUTHOR не задан, можно подставить значение по умолчанию
    if not author:
        author = "Неизвестный автор"
    
    print(f"Автор проекта: {author}")

