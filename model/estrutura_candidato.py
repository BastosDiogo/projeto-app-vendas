
class EstruturaCandidato():
    def __init__(self) -> None:
        self.tipo = 'candidato'

    def estrutura(
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
    
        payload = {
            "nome": nome,
            "cpf": cpf,
            "cargo_atual": cargo_atual,
            "empresa_atual": empresa_atual,
            "nascimento": nascimento,
            "nivel_ingles": nivel_ingles,
            "pretensao_salarial":{
                'minima':pretensao_minima,
                'ideal':pretensao_ideal
            },
            "beneficios": beneficios,
            "contatos": {'email':email,'telefone':telefone},
            "local": {'cidade': cidade,'estado':estado},
            "formacao": formacao,
            "autoriza_lgpd":autoriza_lgpd,
            "linkdin":linkdin
        }

        return payload