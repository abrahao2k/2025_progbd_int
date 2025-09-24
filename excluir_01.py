import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="banco9")
cursor = conexao.cursor()
####################################################################
cod = input("Código do registro a ser excluído: ")

cursor.execute("SELECT * FROM contato WHERE codigo = " + cod)

if cursor.rowcount == 0 :  # se não achou o registro
    print("Registro não encontrado.")

else:

    for linha in cursor:
        print(linha)

    resp = input("Confirma a exclusão? (s/n) ")

    if resp == "s" :
        cursor.execute("DELETE FROM contato WHERE codigo = " + cod)
        conexao.commit()
        print("Excluído com sucesso.")
    else:
        print("Nada foi excluído.")

conexao.close()