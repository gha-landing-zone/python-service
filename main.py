from fastapi import FastAPI

app = FastAPI(title="Hello World", version="0.1.0")


@app.get("/")
async def root():
    return "Hello, World!"


@app.get("/health")
async def health():
    return {"status": "ok"}
