### CONEXÃO ####################################################
import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="acervo")
cursor = conexao.cursor()

### INSERIR ####################################################
def inserir():
    print("### INSERIR LIVRO ###")
    titulo = input("Título do livro: ")
    autor = input("Autor(es): ")
    editora = input("Editora: ")
    
    cursor.execute(
        f"INSERT INTO livros VALUES(null,'{titulo}','{autor}','{editora}')")
    conexao.commit()
    print("INSERIDO COM SUCESSO!\n\n")

### PESQUISAR ################################################
def pesquisar():
    print("### PESQUISAR LIVRO ###")
    busca = input("Digite o titulo/autor/editora: ")
    
    cursor.execute(
    f'''SELECT * FROM livros WHERE titulo LIKE '%{busca}%'
    OR autor LIKE '%{busca}%' OR editora LIKE '%{busca}%' ''')
    
    if cursor.rowcount == 0 :
        print("Nenhum item encontrado.\n\n")
    else:
        for linha in cursor:
            print("Código: " + str(linha[0]) )
            print("Titulo: " + linha[1])
            print("Autor: " + linha[2])
            print("Editora: " + linha[3] + "\n")

### ALTERAR #####################################################
def alterar():
    print("### ALTERAR LIVRO ###")
    codigo = input("Código do livro: ")
    cursor.execute("SELECT * FROM livros WHERE codigo = " + codigo)
    if cursor.rowcount == 0:
        print("Não encontrado. \n\n")
    else:
        for linha in cursor : print (linha)
        resp = input("Deseja alterar? (s/n) ")
        if resp == "s":
            coluna = input("Qual coluna? (titulo/autor/editora) ")
            valor = input("Novo valor: ")
            cursor.execute(
            f"UPDATE livros SET {coluna} = '{valor}' WHERE codigo = {codigo}")
            conexao.commit()
            print("ALTERADO COM SUCESSO.\n\n")

### EXCLUIR LIVRO ##################################################
def excluir():
    print("### EXCLUIR LIVRO ###")
    codigo = input("Código do livro: ")
    cursor.execute("SELECT * FROM livros WHERE codigo = " + codigo)
    if cursor.rowcount == 0:
        print("Não encontrado. \n\n")
    else:
        for linha in cursor : print (linha)
        resp = input("Deseja excluir? (s/n) ")
        if resp == "s":
            cursor.execute(
            f"DELETE FROM livros WHERE codigo = {codigo}")
            conexao.commit()
            print("EXCLUÍDO COM SUCESSO.\n\n")

### MENU DO PROGRAMA ######################################################
while True:
    print("### MENU DO ACERVO DE LIVROS ###")
    print("1-Inserir\n2-Pesquisar\n3-Alterar\n4-Excluir\n5-Sair")
    opcao = input("Qual opção? ")
    
    if   opcao == "1" : inserir()
    elif opcao == "2" : pesquisar()
    elif opcao == "3" : alterar()
    elif opcao == "4" : excluir()
    elif opcao == "5" : break
    else: print("Opção Inválida.")

print("Até a próxima. Fim.")