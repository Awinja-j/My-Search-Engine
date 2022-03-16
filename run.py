import os.path
from search.index import Search


if __name__ == '__main__':
    ss = Search('London Beer Flood')
    print(ss.search())
