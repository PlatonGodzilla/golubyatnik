# Простое FastAPI-приложение

Небольшое приложение, которое возвращает несколько JSON-ответов.

## Локальный запуск

Для запуска требуется Python 3.12 или новее.

1. Клонируйте репозиторий и перейдите в папку проекта:

   ```bash
   git clone https://github.com/PlatonGodzilla/golubyatnik.git
   cd golubyatnik
   ```

2. Создайте виртуальное окружение:

   ```bash
   python3 -m venv venv
   ```

3. Активируйте виртуальное окружение:

   **Windows (CMD):**

   ```bat
   venv\Scripts\activate.bat
   ```

   **Windows (PowerShell):**

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   **macOS и Linux:**

   ```bash
   source venv/bin/activate
   ```

4. Установите зависимости:

   ```bash
   pip install -r ./1/requirements.txt
   ```

5. Перейдите в папку приложения и запустите сервер:

   ```bash
   cd 1
   uvicorn main:app
   ```

Приложение будет доступно по адресу <http://127.0.0.1:8000/>.

## Запуск через Docker

1. Клонируйте репозиторий и перейдите в папку проекта:

   ```bash
   git clone https://github.com/PlatonGodzilla/golubyatnik.git
   cd golubyatnik
   ```

2. Соберите Docker-образ:

   ```bash
   docker build -t fastapiapp ./1/
   ```

3. Запустите контейнер:

   ```bash
   docker run --rm -p 8000:8000 fastapiapp
   ```

Приложение будет доступно по адресу <http://127.0.0.1:8000/>.

## Доступные маршруты

| Метод | Маршрут  | Описание                            |
|-------|----------|-------------------------------------|
| GET   | `/`      | Возвращает приветствие              |
| GET   | `/health` | Возвращает состояние приложения    |
| GET   | `/info`   | Возвращает информацию о приложении |

## CI/CD

При каждом пуше в ветку `main` GitHub Actions собирает Docker-образ и публикует его в GitHub Container Registry (`ghcr.io`). Образу назначаются теги `latest` и `commit-<короткий SHA>`.
