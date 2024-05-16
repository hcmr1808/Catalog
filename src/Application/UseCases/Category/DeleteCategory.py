import psycopg2

class DeleteCategory:
    def __init__(self):
        self.conn = psycopg2.connect(
            database="Filmes",
            user='postgres',
            password='root',
            host="db",
            port=5432,
            client_encoding='utf-8'
        )
    
    def execute(self, id):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT * FROM CATEGORY WHERE id = %s", (id,))
            category_data = cursor.fetchone()

            if not category_data:
                raise ValueError("No category data found")

            cursor.execute("DELETE FROM CATEGORY WHERE id = %s", (id,))          
            self.conn.commit()
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error: {error}")
            self.conn.rollback()
            raise
        finally:
            cursor.close()
    
    def __del__(self):
        self.conn.close()
    