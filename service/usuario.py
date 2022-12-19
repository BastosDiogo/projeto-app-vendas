from model.conexao_mongo import Pymongo
from model.estruturas import EstruturaCliente
from service.tratar_dados import TratarDados
from service.mensagens import Mensagens


class Usuario(Pymongo):
    def __init__(self) -> None:
        super().__init__()
        self.conexao_banco = self.database['usuario']
        self.tratar_dados = TratarDados()
        self.mensagens = Mensagens()

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


    def inserir_usuario(
        self,
        nome_cliente:str,
        cpf:str,
        nascimento:str,
        email:str,
        telefone:str,
        cidade:str,
        estado:str,
        senha:str,
    ):
        """
            A variável "dados_entrada"deve receber um dicionário, com o\n
        seguintes formato:\n
        dados_entrada = {
            nome_cliente: str,\n
            cpf: str,\n
            nascimento: str,\n
            email: str,\n
            telefone: str,\n
            cidade: str,\n
            estado: str\n
        }
            Ou seja, as "keys" da variável "dados_entrada" devem ser os campos\n
        descritos acima, onde seus valores são todos strings.
        """
        
        nome_cliente = str(nome_cliente).upper()
        cpf = self.tratar_dados.tratar_cpf(cpf)
        nascimento = str(nascimento)
        email = str(email).lower()
        telefone = self.tratar_dados.tratar_telefone(telefone)
        cidade = str(cidade).upper()
        estado = str(estado).upper()
        senha = self.tratar_dados.codificar_senha(senha)
        dados = EstruturaCliente().estrutura(
            nome_cliente,
            cpf,
            nascimento,
            email,
            telefone,
            cidade,
            estado,
            senha
        )
        self.conexao_banco.insert_one(dados)

        return True


    def cpfs_na_base(self):
        try:
            cpfs = self.conexao_banco.distinct("cpf",{})
            return cpfs
        
        except Exception as erro:
            print(erro)
            return []


    def verificar_dados_usuario(
        self,
        cpf:str,
        telefone:str,
        email:str,
        senha:str,
        confirmacao_senha:str,
    ):
        cpf = str(cpf)
        senha = str(senha)
        telefone = str(telefone)
        email = str(email).lower()
        confirmacao_senha = str(confirmacao_senha)
        cpfs_na_base = self.cpfs_na_base()

        erros = []
        if cpf in cpfs_na_base:
            erros.append(self.mensagens.mensagem_cpf_repetido())

        if len(cpf) < 11:
            erros.append(self.mensagens.mensagem_cpf_faltando_caracter())

        if len(telefone) <= 9:
            erros.append(self.mensagens.mensagem_telefone_faltando_caracter())

        if '@' not in email:
            erros.append(self.mensagens.mensagem_email_faltando_arroba())

        if senha != confirmacao_senha:
            erros.append(self.mensagens.mensagem_senha_diferente())

        return erros



