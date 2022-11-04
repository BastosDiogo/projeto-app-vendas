from flask import Flask, render_template, request, redirect, session, flash
from service.mercado import Mercado
from service.trazer_precos import TrazPrecos
from service.tratar_dados import TratarDados


app = Flask(__name__)
app.secret_key = 'app-venda-produtos'

# candidatos = Candidatos()

titulo = 'Super Mercado - App venda produtos'
# mensagem_acesso_negado ="""Seu NOME e CPF já constam em nosso banco de dados.
#     Obrigado por sua confiança"""

# mensagem_acesso_negado_cpf ="""O CPF inserido não é válido"""

# mensagem_acesso_negado_cpf_existente = """O CPF inserido já consta em nossa
#     base de dados."""

# mensagem_acesso_permitido = """Você ainda não tem cadastro na Bulleyes.
#     Por favor continue o preencimento"""

@app.route('/')
def pagina_inicial():
    return render_template(
        'pagina_inicial.html', titulo=titulo)


@app.route('/produtos-higiene-pessoal')
def higiene_pessoal():
    precos = TrazPrecos().precos()
    
    pasta_dente = precos['pasta_dente']
    sabonete = precos['sabonete']
    shampoo = precos['shampoo']
    escova_dente = precos['escova_dente']
    algodao_bola =precos['algodao_bola']
    cotonete = precos['cotonete']
    fio_dental = precos['fio_dental']
    papel_hienico = precos['papel_hienico']

    return render_template(
        'higiene_pessoal.html',
        titulo=titulo,
        pasta_dente=pasta_dente,
        sabonete=sabonete,
        shampoo=shampoo,
        escova_dente=escova_dente,
        algodao_bola=algodao_bola,
        cotonete=cotonete,
        fio_dental=fio_dental,
        papel_hienico=papel_hienico,
    )


@app.route('/produtos-bebidas')
def bebidas():
    precos = TrazPrecos().precos()
    
    conhaque = precos['conhaque']
    cerveja_lata_350ml = precos['cerveja_lata_350ml']
    H2O = precos['H2O']
    cerveja_antartica_600ml = precos["cerveja_antartica_600ml"]
    cerveja_heineken_600ml = precos['cerveja_heineken_600ml']
    chopp_vinho_473ml = precos['chopp_vinho_473ml']
    vinho_tinto = precos['vinho_tinto']
    vinho_branco = precos['vinho_branco']

    return render_template(
        'bebidas.html',
        titulo=titulo, 
        conhaque=conhaque,
        cerveja_lata_350ml=cerveja_lata_350ml,
        H2O=H2O,
        cerveja_antartica_600ml=cerveja_antartica_600ml,
        cerveja_heineken_600ml=cerveja_heineken_600ml,
        chopp_vinho_473ml=chopp_vinho_473ml,
        vinho_tinto=vinho_tinto,
        vinho_branco=vinho_branco
    )


@app.route('/produtos-petiscos')
def petiscos():
    precos = TrazPrecos().precos()

    amendoim = precos['amendoim']
    azeitona = precos['azeitona']
    bata_chips = precos['bata_chips']
    fandangos = precos['fandangos']
    pingo_ouro = precos['pingo_ouro']
    queijo_bola = precos['queijo_bola']
    torrada_queijo = precos['torrada_queijo']
    torrada_amanteigada =precos['torrada_amanteigada']

    return render_template(
        'petiscos.html',
        titulo=titulo,
        amendoim=amendoim,
        azeitona=azeitona,
        bata_chips=bata_chips,
        fandangos=fandangos,
        pingo_ouro=pingo_ouro,
        queijo_bola=queijo_bola,
        torrada_queijo=torrada_queijo,
        torrada_amanteigada=torrada_amanteigada
    )



"subir na internet = https://cursos.alura.com.br/forum/topico-onde-hospedar-a-aplicacao-73692"

if __name__ == "__main__":  # Para poder executar quando o arquivo não for importado
    app.run(debug=True)     # Para ir atualizando as modificações que o codigo faz no site

# Heroku: https://dashboard.heroku.com/apps/busca-exp-candidatos/deploy/heroku-git

# Download: https://www.w3schools.com/tags/att_a_download.asp
# Video sobre linkl de download no html = https://www.youtube.com/watch?v=Jszz7M676y8
# Site com os typos de midia: https://www.iana.org/assignments/media-types/media-types.xhtml
# Duvidas hmtl: https://www.w3schools.com/tags/att_a_download.asp


# link:
# https://www.delftstack.com/pt/howto/html/center-a-form-in-html/#:~:text=formul%C3%A1rio%20em%20HTML.-,Use%20a%20propriedade%20CSS%20margin%20para%20centralizar%20um%20formul%C3%A1rio%20em,cont%C3%AAiner%20e%20os%20elementos%20adjacentes.

#Link 2:
# https://pt.stackoverflow.com/questions/148611/centralizar-form-etc-deixar-no-centro-da-tela

# Link 3:
# https://pt.stackoverflow.com/questions/172932/alinhamento-de-bot%C3%B5es-com-css