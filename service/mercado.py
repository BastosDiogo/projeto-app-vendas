from model.conexao_mongo import Pymongo
from model.estruturas import EstruturaProduto, EstruturaCliente


class Mercado(Pymongo):
    def __init__(self) -> None:
        super().__init__()
        self.conexao_banco = self.database['produtos_cadastrados']

    def find(self, filtos:dict, reject:dict):
        try:
            coll = list(self.conexao_banco.find(filtos, reject))
            return coll
        
        except Exception as erro:
            print(erro)

    def aggregate(self, pipeline:list):
        coll = list(self.conexao_banco.aggregate(pipeline))
        
        return coll

    def inserir_produtos(
        self,
        nome_produto:str,
        preco_venda: float,
        quantidade: int,
        tipo_produto = None,
        ml: bool = False,
        litro: bool = False,
        kg: bool = False,
        pacote: bool = False,
    ):
        dados = EstruturaProduto().estrutura(
            nome_produto,
            preco_venda,
            quantidade,
            tipo_produto,
            ml,
            litro,
            kg,
            pacote,
        )

        self.conexao_banco.insert_one(dados)

        return True

    def cpfs_na_base(self):
        try:
            cpfs = list(self.conexao_banco.distinct("cpf",{}))
            return cpfs
        
        except Exception as erro:
            print(erro)        
