from uuid import UUID

from fastapi import Depends, FastAPI

from api_pedidos.esquema import HealthCheckResponse, Item

# ...

app = FastAPI()


@app.get(
    "/healthcheck",
    tags=["healthcheck"],
    summary="Integridade do sistema",
    description="Checa se o servidor está online",
    response_model=HealthCheckResponse,
)
def healthcheck():
    return HealthCheckResponse(status="ok")


# ...
@app.get(
    "/orders/{identificacao_do_pedido}/items",
    summary="Itens de um pedido",
    tags=["pedidos"],
    description="Retorna todos os itens de um determinado pedido",
    response_model=list[Item],
)
def listar_itens(identificacao_do_pedido: UUID):
    pass


def recuperar_itens_por_pedido(identificacao_do_pedido: UUID) -> list[Item]:
    pass


# ...
@app.get(
    "/orders/{identificacao_do_pedido}/items",
    summary="Itens de um pedido",
    tags=["pedidos"],
    description="Retorna todos os itens de um determinado pedido",
    response_model=list[Item],
)
def listar_itens(itens: list[Item] = Depends(recuperar_itens_por_pedido)):
    return itens


from http import HTTPStatus

from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse

from api_pedidos.excecao import PedidoNaoEncontradoError

# ...


@app.exception_handler(PedidoNaoEncontradoError)
def tratar_erro_pedido_nao_encontrado(
    request: Request, exc: PedidoNaoEncontradoError
):
    return JSONResponse(
        status_code=HTTPStatus.NOT_FOUND,
        content={"message": "Pedido não encontrado"},
    )


# ...
