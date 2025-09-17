#importar o driver
import mariadb            # mysql.connector

#criar a conexao
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="banco9")

#criar um cursor que executa comandos sql
cursor = conexao.cursor()

###########################################################

# executar a consulta
cursor.execute("SELECT * FROM contato")

# exibir os dados
for linha in cursor:
    #print(linha)
    print("Código:", linha[0])
    print("Nome:", linha[1])
    print("Telefone:", linha[2])
    print("-------------------------")
    
# fechando a conexao
cursor.close()
conexao.close()
