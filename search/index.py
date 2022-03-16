from .analysis import analyze
from .__init__ import db

DB = db()

class Search:
    def __init__(self, query: str):
        self.query = analyze(query)

    def search_query(self):
        cursor = DB.get_cursor()
        query = '|'.join(self.query)
        cursor.execute(f'SELECT abstract FROM search.documents USE INDEX (ID) WHERE abstract REGEXP \'%{query}%\' OR title REGEXP \'%{query}%\'')
        return cursor.fetchall()

    def search(self) -> list:
        """
        Search; this will return documents that contain words from the query.
        Parameters:
          - query: the query string
        """

        res = self.search_query()
        return res

