from fastapi import  FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from alchemy import session,cruds
from base.models import Contato, Update
from fastapi.staticfiles import StaticFiles


app = FastAPI()


@app.post('/gravar')
def new_contato(contato: Contato):
    cruds.insert_contato(contato.nome,contato.celular)

@app.post('/contatos')
def show_contacts():
    contatos = cruds.get_contatos()
    return contatos

@app.post('/update')
def select_contact(contato: Update):
    print(contato.key)
    cruds.update_contato(contato.nome,contato.celular,contato.key)

@app.post('/delete')
def delete_contact(contato: Contato):
    cruds.delete_contato(contato.celular)


templates = Jinja2Templates(directory = "templates")
@app.get("/", response_class = HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})