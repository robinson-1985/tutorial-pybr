from pydantic import BaseModel


class Item(BaseModel):
    sku: str
    description: str
    image_url: str
    reference: str
    quantity: int


# ...
class HealthCheckResponse(BaseModel):
    status: str


# ...
class ErrorResponse(BaseModel):
    message: str


# ...

"""
# ...
@app.get("/orders/{identificacao_do_pedido}/items", responses={
    HTTPStatus.NOT_FOUND.value: {
        "description": "Pedido não encontrado",
        "model": ErrorResponse,
    },
    HTTPStatus.BAD_GATEWAY.value: {
        "description": "Falha de comunicação com o servidor remoto",
        "model": ErrorResponse,
    }}, summary="Itens de um pedido", tags=["pedidos"], description="Retorna todos os itens de um determinado pedido", response_model=list[Item])
# ...
"""
