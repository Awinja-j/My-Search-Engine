import mysql.connector

class db:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='',
                                           host='localhost')
    def get_cursor(self):
        return self.cnx.cursor() 

    def close(self):
        self.cnx.close()