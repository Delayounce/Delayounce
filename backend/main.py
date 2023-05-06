from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import backend.get_content_to_serve as get_content_to_serve


app = FastAPI()

app.mount("/docs", StaticFiles(directory="docs"), name="docs")
templates = Jinja2Templates(directory="docs")

#start defining urls below

@app.get("/")
async def read_item(request: Request):
    posts = get_content_to_serve.get_x_posts(0,6)
    previous_page = 0
    next_page = 1
    return templates.TemplateResponse("index.html", context= {"request": request,"posts" : posts, "prevP" : previous_page , "nextP" : next_page})

@app.get("/page/{page_number}")
async def read_item(request: Request,page_number):
    posts = []
    html_content = ""
    
    if(int(page_number) < 1):
        previous_page = 0
        page_number = 0
    else:
        previous_page= int(page_number)-1   
         
    next_page = int(page_number)+1

    posts = get_content_to_serve.get_x_posts(int(page_number),6)
    if len(posts) > 1:
        while len(posts) < 6:
            posts.append({
                "userId": -1,
                "id": -1,
                "title": "no more titles",
                "body": "no more posts"
                })
    else:
        html_content = """
        <html>
            <head>
                <title>Static HTML Response</title>
            </head>
            <body>
                <p>how?</p>
                <p>we don't have this many pages</p>
            </body>
        </html>
        """
        return HTMLResponse(content=html_content, status_code=200)

    return templates.TemplateResponse("index.html", context= {"request": request,"posts" : posts, "prevP" : previous_page , "nextP" : next_page})



@app.get ("/about_us", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("about_us.html",{"request":request} )






'''
@app.post("/search/")
async def create_item(search: Search):
    return search
'''
