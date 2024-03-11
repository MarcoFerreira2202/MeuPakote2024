import pymysql

# Configuração da conexão
config = {
    'host': 'seu_host',
    'port': 3306,
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'db': 'seu_banco_de_dados',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

try:
    # Estabelecer a conexão
    connection = pymysql.connect(**config)
    print("Conexão estabelecida com sucesso!")

finally:
    connection.close()
    print("Conexão encerrada.")
