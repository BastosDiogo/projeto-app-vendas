from model.conexao_mongo import Pymongo
from model.estrutura_candidato import EstruturaCandidato

class Candidatos(Pymongo):
    def __init__(self) -> None:
        super().__init__()
        self.conexao_banco = self.database['cadastro_candidatos']

    def find(self, filtos:dict, reject:dict):
        try:
            coll = list(self.conexao_banco.find(filtos, reject))
            return coll
        
        except Exception as erro:
            print(erro)
    
    def inserir_candidato(
        self,
        nome:str,
        cpf:str,
        cargo_atual:str,
        empresa_atual:str,
        nascimento:str,
        nivel_ingles:str,
        pretensao_minima:float,
        pretensao_ideal:float,
        beneficios: str,
        email: str,
        telefone: str,
        cidade: str,
        estado: str,
        formacao: str,
        autoriza_lgpd: bool,
        linkdin: str
    ):
        dados = EstruturaCandidato().estrutura(nome,
        cpf,
        cargo_atual,
        empresa_atual,
        nascimento,
        nivel_ingles,
        pretensao_minima,
        pretensao_ideal,
        beneficios,
        email,
        telefone,
        cidade,
        estado,
        formacao,
        autoriza_lgpd,
        linkdin
        )

        self.conexao_banco.insert_one(dados)

        return True

    def cpfs_na_base(self):
        try:
            cpfs = list(self.conexao_banco.distinct("cpf",{}))
            return cpfs
        
        except Exception as erro:
            print(erro)        
