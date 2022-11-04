
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

    def tratar_nascimento(data:str):
        data = str(data)#.replace('/','-')

        dia = data[0:2]
        mes = data[3:5]
        ano = data[6:10]

        nova_data = f'{ano}-{mes}-{dia}'

        return nova_data

    def tratar_precos(self, preco:float):
        preco = str(preco)
        decimais = preco.split('.')[1]
        # print(decimais)
        if len(decimais) < 2: # Exemplo: preco = '4.5'
            preco = preco + '0'

        novo_preco = preco.replace('.',',')

        return novo_preco

# valor = '4.5'
# x = TratarDados().tratar_precos(valor)