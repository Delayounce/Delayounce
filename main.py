from fastapi import FastAPI
import get_content_func

app = FastAPI()

@app.get("/")
async def root():
    return get_content_func.get_photos()