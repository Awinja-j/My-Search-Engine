import gzip
from lxml import etree
import time

from search.documents import Abstract
import mysql.connector

import logging

logging.basicConfig(filename="loaddata.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 

logs = logging.getLogger()
logs.setLevel(logging.DEBUG)

# Database connection
class LoadDocuments:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='',
                                           host='localhost')


    def get_cursor(self):
        return self.cnx.cursor()

    def close(self):
        self.cnx.close()

    def checkTableExists(self):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM search.documents')
        # if cursor.rowcount == 0:
        self.create_database()
        self.create_table()
        self.insert_data()
        # else:
        #     print('Table already exists')

    def create_database(self):
        cursor = self.get_cursor()
        cursor.execute('CREATE DATABASE IF NOT EXISTS search CHARACTER SET utf8')
        print('Database created')
        cursor.close()

    def create_table(self):
        cursor = self.get_cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS search.documents (ID INT, title VARCHAR(255), url VARCHAR(255), abstract VARCHAR(10000), UNIQUE INDEX (INDEX_ID))')
        cursor.close()
        print('Table created')

    def load_documents(self):
        start = time.time()
        with gzip.open('dataset/enwiki-latest-abstract.xml.gz', 'rb') as f:
            doc_id = 0
            for _, element in etree.iterparse(f, events=('end',), tag='doc'):
                title = element.findtext('./title')
                url = element.findtext('./url')
                abstract = element.findtext('./abstract')

                yield Abstract(ID=doc_id, title=title, url=url, abstract=abstract)

                doc_id += 1
                element.clear()
        end = time.time()
        logs.info(f'Parsing XML took {end - start} seconds')

    def insert_data(self):
        cursor = self.get_cursor()
        try:
            sql = "INSERT INTO search.documents (ID, title, url, abstract) VALUES (%s, %s, %s, %s)"
            cursor.executemany(sql, self.load_documents())
            self.cnx.commit()
            logs.info(f'Inserted document')
        except mysql.connector.errors.DatabaseError as err:
            logs.error(f'Error inserting document')
        cursor.close()
        print('Data inserted')
    
LD = LoadDocuments()
# LD.checkTableExists()
LD.create_table()
LD.insert_data()

