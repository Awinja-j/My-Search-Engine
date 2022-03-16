import sys
from search.index import Search


if __name__ == '__main__':
    ss = Search(sys.argv[1])
    print(ss.search())
