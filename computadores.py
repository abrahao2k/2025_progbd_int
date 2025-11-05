# IMPORTAR O DRIVER
import mariadb

# DADOS DA CONEXÃO
conexao = mariadb.connect(
    host="localhost", user="root",
    password="", database="computadores")

# CURSOR QUE EXECUTA OS COMANDOS SQL
cursor = conexao.cursor()

# MENU DE OPÇÕES
while True:
    print("== MENU ==\n 1-Cadastrar\n 2-Listar\n 3-Pesquisar\n 4-Excluir\n 5-Alterar\n 6-Sair")
    op = input("Opção? ")
    
    if op == "1":
        print("== CADASTRAR COMPUTADOR ==")
        marca = input("Marca: ")
        processador = input("Processador: ")
        memoria = input("Memória: ")
        armazenamento = input("Armazenamento: ")
        
        sql = f'''INSERT INTO pc VALUES (null,'{marca}',
                  '{processador}', {memoria}, {armazenamento})'''
        
        cursor.execute(sql)
        conexao.commit()    #confirma a gravação no banco
        print("INSERIDO COM SUCESSO!\n\n")
    
    elif op == "2":
        print("== LISTAR COMPUTADORES ==")
        
        cursor.execute("SELECT * FROM pc")
        
        for linha in cursor:
            print("Código:", linha[0])
            print("Marca:", linha[1])
            print("Processador:", linha[2])
            print("Memória:", linha[3], "Gb")
            print("Armazenamento:", linha[4], "Gb")
            print("-------------------------------")
        
    elif op == "3":
        print("== PESQUISAR COMPUTADORES ==")
        pesq = input("Termo da pesquisa: ")
        
        sql = f'''SELECT * FROM pc WHERE marca LIKE '%{pesq}%'
                or processador LIKE '%{pesq}%'
                or memoria LIKE '%{pesq}%'
                or armazenamento LIKE '%{pesq}%' '''
        
        cursor.execute(sql)
        
        for linha in cursor:
            print("Código:", linha[0])
            print("Marca:", linha[1])
            print("Processador:", linha[2])
            print("Memória:", linha[3], "Gb")
            print("Armazenamento:", linha[4], "Gb")
            print("-------------------------------")
        
    elif op == "4":
        print("== EXCLUIR COMPUTADOR ==")
        cod = input("Código: ")
        cursor.execute("SELECT * FROM pc WHERE codigo = " + cod)
        
        if cursor.rowcount == 0 :
            print("NÃO ENCONTRADO\n\n")
        
        else:  # se encontrou o código cadastrado
            for linha in cursor:
                print(linha)
            
            resp = input("Deseja excluir? (s/n) ")
            if resp == "s" :
                cursor.execute("DELETE FROM pc WHERE codigo = " + cod)
                conexao.commit()
                print("EXCLUÍDO COM SUCESSO.\n\n")
    
    elif op == "5":
        print("== ALTERAR DADOS DO COMPUTADOR ==")
        cod = input("Código: ")
        cursor.execute("SELECT * FROM pc WHERE codigo = " + cod)
        
        if cursor.rowcount == 0 :
            print("NÃO ENCONTRADO\n\n")
        
        else:  # se encontrou o código cadastrado
            for linha in cursor:
                print(linha)
            
            resp = input("Deseja alterar? (s/n) ")
            if resp == "s" :
                col = input(
                "Qual coluna? (marca/processador/memoria/armazenamento) ")
            
                if col not in ('marca','processador','memoria','armazenamento'):
                    print("COLUNA INVÁLIDA\n\n")
                
                else:
                    valor = input("Novo valor: ")
                    
                    sql = f'''UPDATE pc SET {col} = '{valor}'
                            WHERE codigo = {cod} '''
                    cursor.execute(sql)
                    conexao.commit()
                    print("ALTERADO COM SUCESSO\n\n")
                    
    else:
        conexao.close() # FECHAR A CONEXÃO
        break # SAIR
        
        
            
            
        
          
        