import pandas as pd
from infra.db.MySQL import MySQL

class GetAllTablesRepository:
    def __init__(self, db: MySQL) -> None:
        self.__db = db

    def invoke(self) -> pd.DataFrame:
        conn = self.__db.getConnection()
        rawSql = "SHOW TABLES"
        df = pd.read_sql(rawSql, conn)
        return df