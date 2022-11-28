from model.conexao_mongo import Pymongo

class Admin(Pymongo):
    def __init__(self) -> None:
        super().__init__()
        self.conexao_banco = self.database['admin']
    
    def find(self, filtos:dict, reject:dict):
        try:
            coll = list(self.conexao_banco.find(filtos, reject))
            return coll

        except Exception as erro:
            print(erro)
            return []

    def admins_cadastrados(self, login_admin:str, senha_admin:str):
        login_admin = str(login_admin)
        senha_admin = str(senha_admin)
        admin_cadastrados = self.find(
            {"login":login_admin,"senha":senha_admin},
            {"_id":0}
        )
        resposta = True if len(admin_cadastrados) != 0 else False

        return resposta

