
from service.mercado import Mercado
from service.tratar_dados import TratarDados

class TrazPrecos():
    def __init__(self) -> None:
        self.mercado = Mercado()
        self.tratar_dados = TratarDados()

    def precos(self):
        produtos_bebidas = self.mercado.find(
            {"produto_ativo":True},
            {"_id": 0, "nome_produto": 1, "preco_venda": 1, "id_produto": 1}
        )

        precos = {}
        for produto in produtos_bebidas:
            nome_produto = produto['nome_produto']
            preco_venda = self.tratar_dados.tratar_precos(
                produto['preco_venda']
            )
            precos[nome_produto] = preco_venda

        return precos
