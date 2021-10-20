from http import HTTPStatus
import os
from uuid import UUID
from api_pedidos.esquema import Item
from api_pedidos.excecao import PedidoNaoEncontradoError, FalhaDeComunicacaoError

import httpx

# tenant e apikey fixos somente para demonstrações
APIKEY = os.environ.get("APIKEY", "coloque aqui sua apikey")
TENANT_ID = os.environ.get("TENANT_ID", "21fea73c-e244-497a-8540-be0d3c583596")
MAGALU_API_URL = "https://alpha.api.magalu.com"
MAESTRO_SERVICE_URL = f"{MAGALU_API_URL}/maestro/v1"

def _recupera_itens_por_pacote(uuid_do_pedido, uuid_do_pacote):
    response = httpx.get(
        f"{MAESTRO_SERVICE_URL}/orders/{uuid_do_pedido}/packages/{uuid_do_pacote}/items",
        headers={"X-Api-Key": APIKEY, "X-Tenant-Id": TENANT_ID},
    )
    response.raise_for_status()
    return [
        Item(
            sku=item["product"]["code"],
            # campos que utilizam a função get são opicionais
            description=item["product"].get("description", ""),
            image_url=item["product"].get("image_url", ""),
            reference=item["product"].get("reference", ""),
            quantity=item["quantity"],
        )
        for item in response.json()
    ]

from api_pedidos.excecao import PedidoNaoEncontradoError, FalhaDeComunicacaoError
# ...
@app.exception_handler(FalhaDeComunicacaoError)
def tratar_erro_falha_de_comunicacao(request: Request, exc: FalhaDeComunicacaoError):
    return JSONResponse(status_code=HTTPStatus.BAD_GATEWAY, content={"message": "Falha de comunicação com o servidor remoto"})
# ...
