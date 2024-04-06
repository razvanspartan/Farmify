from API_connector import runFlask
from sqlRepo import SqlConnector

def main():
    sqlConnector = SqlConnector("localhost", "farm", "farmpassword", "farmify")
    runFlask(sqlConnector)


main()
