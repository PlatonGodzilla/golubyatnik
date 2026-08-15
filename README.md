# Просте FastApi приложение

Бесполезное приложение которое показывает пару json-ов

** Запуск локально (требуется установленный Python 3.12+):
    ```git clone https://github.com/PlatonGodzilla/golubyatnik```
    лучше установить виртуальное окружение в папку проекта:
        ```python3 -m venv venv```
        Активация окружения
            Windows (CMD): venv\Scripts\activate.batWindows 
            (PowerShell): .\venv\Scripts\Activate.ps1
            macOS и Linux: source venv/bin/activate
    установите требуемые библиотеки:
        ```pip install -r ./1/requirements.txt```
    потом ```uvicorn main:app``` из папки 1

** Запуск локально (через Docker):
    ```git clone https://github.com/PlatonGodzilla/golubyatnik```
    из папки проекта ```docker build -t fastapiapp ./1/```
    ```docker run -p 8000 fastapiapp```
    в браузере http://127.0.0.1:8000/
    роуты: /, /health, /info

** как работает мой CI/CD
    при кажом пуше в репу, проводится сборка образа на раннере и затем образ пушится на ghcr.io