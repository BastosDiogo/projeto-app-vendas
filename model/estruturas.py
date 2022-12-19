
from uuid import uuid1


class EstruturaProduto():
    def __init__(self) -> None:
        self.tipo = 'produto'

    def estrutura(
        self,
        nome_produto:str,
        preco_venda: float,
        quantidade: int,
        tipo_produto: str = None,
        ml: bool = False,
        litro: bool = False,
        kg: bool = False,
        pacote: bool = False,
    ):
    
        payload = {
            "nome_produto": nome_produto,
            "id_produto": str(uuid1()),
            "preco_venda": preco_venda,
            "quantidade": quantidade,
            "acondicionamento":{
                "ml": ml,
                "litro": litro,
                "kg": kg,
                "pacote": pacote,
            },
            "produto_ativo": True,
            "tipo_produto": tipo_produto,
        }

        return payload


class EstruturaCliente():
    def __init__(self) -> None:
        self.tipo = 'cliente'

    def estrutura(
        self,
        nome:str,
        cpf:str,
        nascimento:str,
        email: str,
        telefone: str,
        cidade: str,
        estado: str,
        senha
    ):
    
        payload = {
            "nome": nome,
            "cpf": cpf,
            "nascimento": nascimento,
            "contatos": {'email':email,'telefone':telefone},
            "local": {'cidade': cidade,'estado':estado},
            "senha": senha
        }

        return payload