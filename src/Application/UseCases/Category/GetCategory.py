import psycopg2

class GetCategory:

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
            print(id)
            cursor.execute("SELECT * FROM CATEGORY WHERE id = %s",(id,))
            category = cursor.fetchone()
            return category
        except psycopg2.Error as e:
            return False, f"Error getting category: {e}"    
        finally:
            cursor.close()    