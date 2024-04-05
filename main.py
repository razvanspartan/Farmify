from API_connector import runFlask
from sqlRepo import SqlConnector

def main():
    sqlConnector = SqlConnector("hostPlaceholder", "user", "password", "database")
    runFlask(sqlConnector)


main()
