# importar o driver do banco
import mariadb
print("Driver carregado.")

# estabelecer a conexao
conexao = mariadb.connect(
    host="localhost", user="root",
    password="", database="banco9" )

print("Conexão estabelecida.")

# criar um "cursor" que permite executar comandos sql
cursor = conexao.cursor()

print("Cursor criado.")

# executar um comando
cursor.execute(
    "INSERT INTO contato VALUES(2,'Beto','9987-4564')" )

# confirmar a gravação dos dados
conexao.commit()
print("Gravado com sucesso.")

