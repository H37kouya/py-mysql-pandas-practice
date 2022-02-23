from infra.db.MySQL import MySQL
from repository.employees.GetAllEmployeesRepository import GetAllEmployeesRepository
from repository.tables.GetAllTablesRepository import GetAllTablesRepository

def hello() -> None:
    # MySQLインスタンスを生成
    db = MySQL()
    db.test()

    # テーブルリポジトリを生成
    getAllTablesRepository = GetAllTablesRepository(db)
    allTables = getAllTablesRepository.invoke()
    print(allTables)

    # Employeeリポジトリを生成
    getAllEmployees = GetAllEmployeesRepository(db)
    allEmployees = getAllEmployees.invoke()
    print(allEmployees)

if __name__ == "__main__":
    hello()
