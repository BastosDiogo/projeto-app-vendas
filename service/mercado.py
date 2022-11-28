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
            return []

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

    def nomes_produtos(self, ids_produtos:list):
        nomes_e_ids = self.find(
            {"id_produto":{"$in":ids_produtos}},
            {"_id":0,"id_produto":1, "nome_produto": 1,}
        )
        nomes_produtos = [produto['nome_produto'] for produto in nomes_e_ids]

        return nomes_produtos


    def atualizar_precos(self, produtos_modificados:dict):
        ids_produtos = []
        for id_produto, preco in produtos_modificados.items():
            if float(preco) != 0:
                id_produto = str(id_produto)
                preco = float(preco)
                ids_produtos.append(id_produto)
                self.update(
                    {"id_produto":id_produto},
                    {"$set":{"preco_venda":preco}}
                )
                print(f'\nProduto: {id_produto}\nNovo preço: {preco}')
        
        if len(ids_produtos) == 0:
            print('Não existe produtos para atualizar')

        nomes_produtos = self.nomes_produtos(ids_produtos)

        return nomes_produtos


    def update(self, filtro:dict, update:dict):
        try:
            self.conexao_banco.update(filtro,update)
            return True
        
        except Exception as erro:
            print(erro)
            return False

    def cpfs_na_base(self):
        try:
            cpfs = list(self.conexao_banco.distinct("cpf",{}))
            return cpfs
        
        except Exception as erro:
            print(erro)
