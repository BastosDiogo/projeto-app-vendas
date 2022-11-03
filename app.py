from flask import Flask, render_template, request, redirect, session, flash
from service.candidato import Candidatos
from service.tratar_dados import (
    tratar_dinheiro,
    tratar_lgpd,
    tratar_nascimento,
)


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
    preco = "15,55"
    return render_template(
        'higiene_pessoal.html', titulo=titulo, preco=preco)


@app.route('/produtos-bebidas')
def bebidas():
    preco = "15,55"
    # xxx = request.from_values('nome-produto')
    # print(f'\n{xxx}\n')
    return render_template(
        'bebidas.html', titulo=titulo, preco=preco)


@app.route('/produtos-petiscos')
def petiscos():
    preco = "15,55"
    return render_template(
        'petiscos.html', titulo=titulo, preco=preco)



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