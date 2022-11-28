
from service.mercado import Mercado
from service.tratar_dados import TratarDados

class TrazPrecos():
    def __init__(self) -> None:
        self.mercado = Mercado()
        self.tratar_dados = TratarDados()

    def precos(self, tipo_produto:str):
        tipo_produto = str(tipo_produto)
        produtos = self.mercado.find(
            {"produto_ativo":True,"tipo_produto": tipo_produto},
            {"_id": 0, "nome_produto": 1, "preco_venda": 1, "id_produto": 1}
        )

        precos = {}
        for produto in produtos:
            id_produto = produto['id_produto']
            preco_venda = self.tratar_dados.tratar_precos(
                produto['preco_venda']
            )
            precos[id_produto] = preco_venda

        return precos
