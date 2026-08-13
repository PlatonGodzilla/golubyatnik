from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return {
        "message": "Hello from FastAPI"
        }

@app.get("/health")
async def health():
    return {
        "status": "ok"
        }

@app.get("/info")
async def info():
    return {
        "app": "devops-test",
        "version": "1.0.0",
        "port": 8000
        }