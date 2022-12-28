from hashlib import sha256
class TratarDados():
    def __init__(self) -> None:
        pass

    def tratar_lgpd(entrada:str):
        entrada = str(entrada).upper()
        if entrada == 'SIM':
            resposta = True
        else:
            resposta = False
        
        return resposta


    def tratar_dinheiro(valor:str):
        valor = str(valor).replace('.','').replace(',','.')
        resposta = float(valor)
        
        return resposta

    def tratar_nascimento(self, data:str):
        data = str(data)#.replace('/','-')

        dia = data[8:10]
        mes = data[5:7]
        ano = data[0:4]

        nova_data = f'{dia}/{mes}/{ano}'

        return nova_data

    def codificar_senha(self, senha:str):
        senha = str(senha)        
        senha = senha.encode()
        hash_senha = sha256(senha)
        # print(hash_senha.hexdigest())
        hash_senha = hash_senha.hexdigest()
        return hash_senha

    def tratar_telefone(self, telefone:str):
        telefone = str(telefone)
        if '(' in telefone or ')' in telefone:
            telefone = telefone.replace(')','')
            telefone = telefone.replace('(','')
            telefone = telefone.replace('-','')

        return telefone

    def tratar_cpf(self, cpf:str):
        cpf = str(cpf).replace('.','')
        cpf = str(cpf).replace('-','')
        return cpf

    def mascara_cpf(self,cpf):
        cpf = str(cpf)
        parte_1 = cpf[0:3]
        parte_2 = cpf[3:6]
        parte_3 = cpf[6:9]
        parte_4 = cpf[9:11]
        cpf_novo = f'{parte_1}.{parte_2}.{parte_3}-{parte_4}'

        return cpf_novo

    def tratar_precos(self, preco:float):
        preco = str(preco)
        decimais = preco.split('.')[1]
        # print(decimais)
        if len(decimais) < 2: # Exemplo: preço = '4.5'
            preco = preco + '0'

        novo_preco = preco.replace('.',',')

        return novo_preco
