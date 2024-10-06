from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import Pyro4

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calcular")
async def calcular(request: Request, numero: int = Form(...)):
    # Conectar con el servidor Pyro4
    uri = "PYRO:FactorialServer@localhost:9090"  # Modificar con tu URI
    factorial_server = Pyro4.Proxy(uri)
    result = factorial_server.factorial(numero)
    return templates.TemplateResponse("index.html", {"request": request, "result": result})
