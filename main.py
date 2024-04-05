from API_connector import runFlask
from sqlRepo import SqlConnector

def main():
    sqlConnector = SqlConnector("104.248.193.68", "farm", "farmpassword", "farmify")
    runFlask(sqlConnector)


main()
