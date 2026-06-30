import os
from dotenv import load_dotenv

# Загружаем переменные из .env (должен лежать рядом с main.py)
load_dotenv()

def print_author():
    author = os.getenv("AUTHOR")
    
    if not author:
        author = "Неизвестный автор"
    
    print(f"Автор проекта: {author}")

# ЭТОГО НЕ ХВАТАЛО: точка входа, которая запускает функцию
if __name__ == "__main__":
    print_author()

