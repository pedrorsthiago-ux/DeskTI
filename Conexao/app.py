
from flask import Flask, render_template, request, session, redirect
from conexao import conectar_banco
from werkzeug.security import check_password_hash

import os

pasta_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=pasta_projeto,
    static_folder=pasta_projeto,
    static_url_path="/arquivos"
)

app.secret_key = "deskti_chave_secreta"


# PAGINA INICIAL - LOGIN

@app.route("/")
def inicio():
    return render_template("FormLogin/fss.html")


# LOGIN

@app.route("/login", methods=["GET"])
def abrir_login():
    return render_template("FormLogin/fss.html")


@app.route("/login", methods=["POST"])
def login():
    try:
        banco = conectar_banco()
        cursor = banco.cursor(dictionary=True)

        email = request.form["email"]
        senha = request.form["senha"]

        sql = "SELECT * FROM usuarios WHERE email = %s"
        cursor.execute(sql, (email,))

        usuario = cursor.fetchone()

        cursor.close()
        banco.close()

        if usuario and check_password_hash(usuario["senha"], senha):
            session["usuario_id"] = usuario["id"]
            return redirect("/equipamentos")

        return "E-mail ou senha incorretos!"

    except Exception as erro:
        return f"Erro ao realizar login: {erro}"


# FORMULARIO DE EQUIPAMENTOS

@app.route("/equipamentos", methods=["GET"])
def abrir_equipamentos():
    if "usuario_id" not in session:
        return redirect("/")

    return render_template("src/FormEquipamentos/fe.html")


# SALVAR SOLICITACAO DE EQUIPAMENTOS

@app.route("/salvar-solicitacao", methods=["POST"])
def salvar_solicitacao():
    try:
        if "usuario_id" not in session:
            return redirect("/")

        banco = conectar_banco()
        cursor = banco.cursor()

        sql = """
            INSERT INTO solicitacoes
            (usuario_id, tipo, equipamento, descricao, status)
            VALUES (%s, %s, %s, %s, %s)
        """

        valores = (
            session["usuario_id"],
            request.form["tipo"],
            request.form["equipamento"],
            request.form["descricao"],
            "Pendente"
        )

        cursor.execute(sql, valores)
        banco.commit()

        cursor.close()
        banco.close()

        return redirect("/agendamento")

    except Exception as erro:
        return f"Erro ao salvar solicitação: {erro}"


# FORMULARIO DE AGENDAMENTO

@app.route("/agendamento", methods=["GET"])
def abrir_agendamento():
    if "usuario_id" not in session:
        return redirect("/")

    return render_template("FormAgendamento/FA.html")


# SALVAR AGENDAMENTO

@app.route("/salvar-agendamento", methods=["POST"])
def salvar_agendamento():
    try:
        if "usuario_id" not in session:
            return redirect("/")

        banco = conectar_banco()
        cursor = banco.cursor()

        sql = """
            INSERT INTO agendamentos
            (nome, email, matricula, telefone, servico,
             data_agendamento, horario, descricao)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            request.form["Nome"],
            request.form["Email"],
            request.form["Matricula"],
            request.form["Telefone"],
            request.form["Servico"],
            request.form["Data"],
            request.form["Horario"],
            request.form["Descricao"]
        )

        cursor.execute(sql, valores)
        banco.commit()

        cursor.close()
        banco.close()

        return "Agendamento salvo com sucesso!"

    except Exception as erro:
        return f"Erro ao salvar agendamento: {erro}"


if __name__ == "__main__":
    app.run(debug=True)
