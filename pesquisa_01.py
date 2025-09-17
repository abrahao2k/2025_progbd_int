#importar o driver
import mariadb            # mysql.connector

#criar a conexao
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="banco9")

#criar um cursor que executa comandos sql
cursor = conexao.cursor()

###########################################################

print("=== PESQUISA DE CONTATO ===")
nome = input("Digite o nome: ")

cursor.execute(f" SELECT * FROM contato WHERE nome LIKE '%{nome}%' ")

for linha in cursor:
    print("Código:", linha[0])
    print("Nome:", linha[1])
    print("Telefone:", linha[2])
    print("-----------------------")
    

print(cursor.rowcount, "registros encontrados.")

cursor.close()
conexao.close()