from conexao import conectar_banco
from werkzeug.security import generate_password_hash

banco = conectar_banco()
cursor = banco.cursor()

nome = "Usuario Teste"
email = "teste@deskti.com"
senha = generate_password_hash("123456")
tipo_usuario = "Aluno"

sql = """
INSERT INTO usuarios (nome, email, senha, tipo_usuario)
VALUES (%s, %s, %s, %s)
"""

valores = (nome, email, senha, tipo_usuario)

cursor.execute(sql, valores)
banco.commit()

print("Usuário cadastrado com sucesso!")

cursor.close()
banco.close()