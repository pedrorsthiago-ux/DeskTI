from conexao import conectar_banco

try:
    banco = conectar_banco()
    print("Conexão com o MySQL realizada!")

    cursor = banco.cursor()
    cursor.execute("SELECT DATABASE()")

    resultado = cursor.fetchone()
    print("Banco conectado:", resultado[0])

    cursor.close()
    banco.close()

except Exception as erro:
    print("Erro ao conectar:", erro)