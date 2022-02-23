import pandas as pd
from infra.db.MySQL import MySQL

class GetAllEmployeesRepository:
    def __init__(self, db: MySQL) -> None:
        self.__db = db

    def invoke(self) -> pd.DataFrame:
        conn = self.__db.getConnection()
        rawSql ='''\
            SELECT
                emp_no
                , birth_date
                , first_name
                , last_name
                , gender
                , hire_date
            FROM
                employees
        '''
        df = pd.read_sql(rawSql, conn)
        return df
