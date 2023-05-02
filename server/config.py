import mysql.connector

# cria uma conexão com o banco de dados
cnx = mysql.connector.connect(user='Bayonetta', password='$Mika2023', host='127.0.0.1', database='bayo_portal_garanhuns_bd')

# cria um cursor para executar consultas
cursor = cnx.cursor()

# executa uma consulta simples
query = ("SELECT nome FROM pontos_turisticos")
cursor.execute(query)

# recupera os resultados da consulta
for (nome,) in cursor:
    print(nome)

# fecha o cursor e a conexão
cursor.close()
cnx.close()
