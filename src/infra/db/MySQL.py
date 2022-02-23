import mysql.connector

class MySQL:
    def __init__(self) -> None:
        self.__conn = mysql.connector.connect(
            host='db',
            port='3306',
            user='tester',
            password='tester',
            database='employees',
        )

    def __del__(self) -> None:
        self.__conn.close()
        print('Disconnected from MySQL')

    # 接続テスト
    def test(self) -> None:
        conn = self.getConnection()
        if conn.is_connected():
            print('Connected to MySQL')

            print("Connected test to MySQL")
            cursor = conn.cursor()
            cursor.execute("SELECT VERSION()")
            result = cursor.fetchone()
            print(result)
            cursor.close()
        else:
            print('Not connected to MySQL')
            raise Exception('Not connected to MySQL')

    def getConnection(self) -> mysql.connector.connection.MySQLConnection:
        return self.__conn