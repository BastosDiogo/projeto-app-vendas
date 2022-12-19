
class Mensagens():
    def __init__(self) -> None:
        pass

    def mensagem_acesso_permitido(self, acesso_admin:bool):
        if acesso_admin == True:
            mensagem = """Administrador Autenticado com sucesso."""
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

    def mensagem_cpf_repetido(self):
        mensagem = """CPF do cliente, ja cadastrado na base."""
        return mensagem

    def mensagem_cpf_faltando_caracter(self):
        mensagem = """CPF inválido. O CPF deve ter 11 caracteres."""
        return mensagem

    def mensagem_senha_diferente(self):
        mensagem = f"""O campo "senha" e o "confirmar senha" devem ser iguais."""
        return mensagem

    def mensagem_telefone_faltando_caracter(self):
        mensagem = """Telfone inválido. O Telfone deve ter 11 caracteres,
         contando com o DDD."""
        return mensagem

    def mensagem_email_faltando_arroba(self):
        mensagem = """Email inválido. Por favor inserir um email válido."""
        return mensagem

    def mensagem_cliente_cadastrado(self):
        mensagem = """Cliente cadastrado com sucesso."""
        return mensagem