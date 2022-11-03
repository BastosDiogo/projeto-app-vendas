
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

