from src.Domain.Entity.Category import Category
import psycopg2

class UpdateCategory:
    def __init__(self):
        self.conn = psycopg2.connect(
            database="Filmes",
            user='postgres',
            password='root',
            host="db",
            port=5432,
            client_encoding='utf-8'
        )
    
    def execute(self, id, name, description):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT * FROM CATEGORY WHERE id = %s", (id,))
            category_data = cursor.fetchone()

            if not category_data:
                raise ValueError("No category data found")

            category = Category(category_data[1], category_data[2], category_data[3])
            category.Update(name, description) 

            cursor.execute("UPDATE CATEGORY SET name = %s, description = %s WHERE id = %s", (category.name, category.description, id))          
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error: {error}")
        finally:
            cursor.close()
    
    def __del__(self):
        self.conn.close()