from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import backend.get_content_func as get_content_func


app = FastAPI()

app.mount("/docs", StaticFiles(directory="docs"), name="docs")

templates = Jinja2Templates(directory="docs")

@app.get("/")
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", context= {"request": request})




@app.get ("/about_us", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("about_us.html",{"request":request} )






'''
@app.post("/search/")
async def create_item(search: Search):
    return search
'''
