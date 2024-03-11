import psycopg2

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname = 'my_db',
            user = 'postgres',
            password = 'postgres',
            host = 'localhost',
            port='5432'
        )

        self.cursor = self.connection.cursor()
    
    def db_session(self):
        return self.connection
    
    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def close(self):
        self.connection.close()

        