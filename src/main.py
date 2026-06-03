import uvicorn
from handlers.figurinha_handler import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

@app.get("/")
async def main():
    return {"teste"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)