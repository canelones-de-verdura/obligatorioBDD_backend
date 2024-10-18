import mysql.connector

class Consultor:
    def __init__(self: object, passwd: str) -> object:
        try:
            self.cnx = mysql.connector.connect(
                user='root',
                password=passwd,
                host='64.23.228.143',
                database='escuela_deportes'
            )
            self.cursor = self.cnx.cursor(dictionary=True)
        except mysql.connector.Error as err:
            self.msg = err
        else:
            self.msg = "OK"

    def run_query(self: object, query: str):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            return err

    def end_connection(self: object):
        self.cursor.close()
        self.cnx.close()
