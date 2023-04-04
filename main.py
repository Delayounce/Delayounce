from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import get_content_func


app = FastAPI()

app.mount("/Frontend", StaticFiles(directory="Frontend"), name="Frontend")

templates = Jinja2Templates(directory="Frontend")

@app.get("/")
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", context= {"request": request})



@app.get("/posty/{test}", response_class=HTMLResponse)
def write_variable(request: Request, test: int):

    
    test = get_content_func.get_post()[test-1]["body"]

    return templates.TemplateResponse("DisplayPosts.html",{"request":request, "test":test} )


@app.get("/photo/{photoID}", response_class=HTMLResponse)
def write_variable(request: Request, photoID: int):

    
    photoID = get_content_func.get_photos()[photoID-1]["url"]

    return templates.TemplateResponse("DisplayPhotos.html",{"request":request, "photoID":photoID} )