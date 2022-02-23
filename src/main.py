from infra.db.MySQL import MySQL
from repository.tables.GetAllTablesRepository import GetAllTablesRepository

def hello() -> None:
    # MySQLインスタンスを生成
    db = MySQL()
    db.test()

    # テーブルリポジトリを生成
    getAllTablesRepository = GetAllTablesRepository(db)
    allTables = getAllTablesRepository.invoke()
    print(allTables)

if __name__ == "__main__":
    hello()
