from flask import Flask, render_template, request, redirect, session, flash
from service.mercado import Mercado
from service.trazer_precos import TrazPrecos
from service.tratar_dados import TratarDados
from service.mensagens_usuario import MensagemUsuario
from service.admin import Admin


app = Flask(__name__)
app.secret_key = 'app-venda-produtos'

# candidatos = Candidatos()

titulo = 'Super Mercado - App venda produtos'
mercado = Mercado()
mensagem_usurio = MensagemUsuario()
admin_sistema = Admin()
# mensagem_acesso_negado ="""Seu NOME e CPF já constam em nosso banco de dados.
#     Obrigado por sua confiança"""

# mensagem_acesso_negado_cpf ="""O CPF inserido não é válido"""

# mensagem_acesso_negado_cpf_existente = """O CPF inserido já consta em nossa
#     base de dados."""

# mensagem_acesso_permitido = """Usuário Autenciado com sucesso."""
# mensagem_modificaco_preco = """
#     Preços modificados. Caso deseje alterár-los novamente, redigite os novos preços.
#     """

@app.route('/')
def pagina_inicial():
    return render_template(
        'pagina_inicial.html', titulo=titulo)


@app.route('/produtos-higiene-pessoal')
def higiene_pessoal():
    precos = TrazPrecos().precos("higiene")
    
    pasta_dente = precos['6c4359df-5bc3-11ed-88bb-24f5aaf0a4bc']
    sabonete = precos['6cbe566c-5bc3-11ed-b190-24f5aaf0a4bc']
    shampoo = precos['6d2666dc-5bc3-11ed-b6bb-24f5aaf0a4bc']
    escova_dente = precos['6d8f61f6-5bc3-11ed-afb8-24f5aaf0a4bc']
    algodao_bola =precos['6dfddb2d-5bc3-11ed-aca7-24f5aaf0a4bc']
    cotonete = precos['6e9e12d8-5bc3-11ed-ad8c-24f5aaf0a4bc']
    fio_dental = precos['6f033d51-5bc3-11ed-a42d-24f5aaf0a4bc']
    papel_hienico = precos['6f8390c6-5bc3-11ed-8e4e-24f5aaf0a4bc']

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
    precos = TrazPrecos().precos("bebida")
    
    conhaque = precos['5b1cfeff-5bb0-11ed-9dd1-24f5aaf0a4bc']
    cerveja_lata_350ml = precos['3124e9f0-5bb0-11ed-a729-24f5aaf0a4bc']
    H2O = precos['31b89e43-5bb0-11ed-ae6f-24f5aaf0a4bc']
    cerveja_antartica_600ml = precos["322d801a-5bb0-11ed-8421-24f5aaf0a4bc"]
    cerveja_heineken_600ml = precos['32962d08-5bb0-11ed-a92a-24f5aaf0a4bc']
    chopp_vinho_473ml = precos['32fe1697-5bb0-11ed-b06f-24f5aaf0a4bc']
    vinho_tinto = precos['33ce10ec-5bb0-11ed-9500-24f5aaf0a4bc']
    vinho_branco = precos['34364879-5bb0-11ed-9ce0-24f5aaf0a4bc']

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
    precos = TrazPrecos().precos("petisco")

    amendoim = precos['3cf71d50-5bc4-11ed-8f9b-24f5aaf0a4bc']
    azeitona = precos['3d6aba3e-5bc4-11ed-9a37-24f5aaf0a4bc']
    bata_chips = precos['3dd09579-5bc4-11ed-b8b5-24f5aaf0a4bc']
    fandangos = precos['3e69c84b-5bc4-11ed-a16a-24f5aaf0a4bc']
    pingo_ouro = precos['3ef741bb-5bc4-11ed-840b-24f5aaf0a4bc']
    queijo_bola = precos['3f6e8dd8-5bc4-11ed-801b-24f5aaf0a4bc']
    torrada_queijo = precos['3fd76fa2-5bc4-11ed-8497-24f5aaf0a4bc']
    torrada_amanteigada =precos['4082ec82-5bc4-11ed-92fb-24f5aaf0a4bc']

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
# methods = ['POST',]
@app.route('/verificar-admin')
def verificar_admin():
    return render_template(
        'verificar_admin.html', titulo=titulo)

@app.route('/autenticar',methods = ['POST',])
def autenticar():
    login = request.form['login']
    senha = request.form['senha']
    admins_cadastrados = admin_sistema.admins_cadastrados(login,senha)

    if admins_cadastrados:
        flash(mensagem_usurio.mensagem_acesso_permitido(True))
        return redirect('/area-admin')

    flash(mensagem_usurio.mensagem_acesso_permitido(False))
    return render_template('verificar_admin.html')


@app.route('/area-admin', methods = ['POST','GET'])
def area_admin():
    return render_template('area_admin.html', titulo=titulo)


@app.route('/precos-atualizados', methods = ['POST','GET'])
def precos_modificados():
    precos_inseridos_usuario = request.form
    precos_atualizados = mercado.atualizar_precos(precos_inseridos_usuario)
    flash(mensagem_usurio.mensagem_modificaco_preco(precos_atualizados))

    return render_template('area_admin.html', titulo=titulo)



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