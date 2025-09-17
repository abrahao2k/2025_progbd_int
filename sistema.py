from conectarbd import *

while True:
    
    print("=== MENU ===\n1-CADASTRAR\n2-PESQUISAR\n3-SAIR")
    op = input("Opção? ")

    if op == "1":
        print("=== CADASTRO ===")
        nome = input("Nome: ")
        tel  = input("Telefone: ")
        cursor.execute(
            f" INSERT INTO contato VALUES(null,'{nome}','{tel}') ")
        conexao.commit()
        print("Gravado com sucesso.")

    elif op == "2":
        print("=== PESQUISA ===")
        nome = input("Nome: ")
        cursor.execute(
            f"SELECT * FROM contato WHERE nome LIKE '%{nome}%' ")
        for linha in cursor:
            print(linha)
            print(cursor.rowcount, "registros encontrados")

    else:
        print("Fim da execução.")
        break
