import psycopg2

class ConexaoFactory:
    def get_conexao(self):
        return psycopg2.connect(host='localhost',
                                 database='livraria',
                                 user='postgres',
                                 password='Sabesp@22')


