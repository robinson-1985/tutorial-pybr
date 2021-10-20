from fastapi import FastAPI
from fastapi import FastAPI, Depends
from api_pedidos.esquema import Item
# ...

app = FastAPI()

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}

from uuid import UUID

# ...

@app.get("/orders/{identificacao_do_pedido}/items")
def listar_itens(identificacao_do_pedido: UUID):
    pass

def recuperar_itens_por_pedido(identificacao_do_pedido: UUID) -> list[Item]:
    pass

# ...

@app.get("/orders/{identificacao_do_pedido}/items")
def listar_itens(itens: list[Item] = Depends(recuperar_itens_por_pedido)):
    return itens

from api_pedidos.excecao import PedidoNaoEncontradoError
from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
from http import HTTPStatus
# ...

@app.exception_handler(PedidoNaoEncontradoError)
def tratar_erro_pedido_nao_encontrado(request: Request, exc: PedidoNaoEncontradoError):
    return JSONResponse(status_code=HTTPStatus.NOT_FOUND, content={"message": "Pedido não encontrado"})

# ...
