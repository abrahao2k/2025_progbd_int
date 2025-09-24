import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="banco9")
cursor = conexao.cursor()
####################################################################
cod = input("Código do registro a ser alterado: ")

cursor.execute("SELECT * FROM contato WHERE codigo = " + cod)

for linha in cursor:
    print("\ncódigo: " + str(linha[0]))
    print("nome: " + linha[1])
    print("telefone: " + linha[2] + "\n")
    
coluna = input("Qual coluna alterar? (nome/telefone) ")
valor = input("Digite o novo valor: ")

if coluna == "nome" :
    cursor.execute(f"UPDATE contato SET nome = '{valor}' WHERE codigo = {cod}")
    conexao.commit()
    print("Atualizado com sucesso.")

elif coluna == "telefone" :
    cursor.execute(f"UPDATE contato SET telefone = '{valor}' WHERE codigo = {cod}")
    conexao.commit()
    print("Atualizado com sucesso.")
