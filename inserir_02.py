import mariadb

conexao = mariadb.connect(
    host="localhost", user="root",
    password="", database="banco9" )

cursor = conexao.cursor()

# solicitar a digitação dos dados
nome = input("Nome: ")
telefone = input("Telefone: ")

# executar o comando inserindo as variáveis
cursor.execute(f'''INSERT INTO contato VALUES(null,
'{nome}', '{telefone}')''' )

conexao.commit()
print("Gravado com sucesso.")
