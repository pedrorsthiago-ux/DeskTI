import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv(
    dotenv_path=os.path.join(os.path.dirname(__file__), ".env"),
    override=True
)

def conectar_banco():
    conexao = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 3307)),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME"),
        use_pure=True
    )

    return conexao