
class MensagemUsuario():
    def __init__(self) -> None:
        pass

    def mensagem_acesso_permitido(self, acesso_admin:bool):
        if acesso_admin == True:
            mensagem = """Usuário Autenciado com sucesso."""
        else:
            mensagem = """ACESSO NEGADO. O Login e/ou senha estão incorretos."""
        
        return mensagem

    def mensagem_modificaco_preco(self, produtos_atualizados: list):
        if len(produtos_atualizados) != 0:
            produto_front = ''
            contador = 0
            for produto in produtos_atualizados:
                if len(produtos_atualizados) == 1:
                    produto_front = produto
                    continue

                # while contador < len(produtos_atualizados) :
                #     produto_front += f'{produto}, '
                #     contador += 1
                # produto_front += f'e {produto}'

                contador += 1

                if contador == len(produtos_atualizados):
                    produto_front += f'e {produto}'
                    produto_front = produto_front.replace(', e', ' e ')
                    continue

                produto_front += f'{produto}, '
                    
            mensagem = f"""
                Produtos modificados: {produto_front}.\n
                Caso deseje alterár-los novamente, redigite os novos preços.
            """
        else:
            mensagem = """Nenhum preço novo foi inserido.
                Não foi possível alterar os preços.
                """
        return mensagem

    # mensagem_acesso_negado ="""Seu NOME e CPF já constam em nosso banco de dados.
#     Obrigado por sua confiança"""

# mensagem_acesso_negado_cpf ="""O CPF inserido não é válido"""