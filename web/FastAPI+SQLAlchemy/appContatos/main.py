from fastapi import  FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from alchemy import session,cruds
from base.models import Contato



app = FastAPI()
@app.post('/gravar')
def new_contato(contato: Contato):
    cruds.insert_contato(session.my_session,contato)

@app.get('/contatos')
def show_contacts():
    contatos = cruds.get_contatos(session.my_session)
    return contatos

templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})