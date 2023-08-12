from fastapi import  FastAPI,Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from alchemy import session,cruds
from base.models import Contato, Update
from fastapi.staticfiles import StaticFiles

from fastapi.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post('/gravar', response_class = RedirectResponse, status_code=302)
def new_contato(nome: str = Form(), celular: str = Form()):
    cruds.insert_contato(nome,celular)
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)

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
    contatos = cruds.get_contatos()
    return templates.TemplateResponse("index.html",{"request":request, "contatos":contatos})