import mariadb

conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="banco9")

cursor = conexao.cursor()

