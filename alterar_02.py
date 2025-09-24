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

if coluna in ("nome", "telefone") :
    valor = input("Digite o novo valor: ")
    cursor.execute(f"UPDATE contato SET {coluna} = '{valor}' WHERE codigo = {cod}")
    conexao.commit()
    print("Atualizado com sucesso.")
else:
    print("A coluna informada não existe.")

conexao.close()