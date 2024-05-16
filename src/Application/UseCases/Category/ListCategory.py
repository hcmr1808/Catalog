from src.Domain.Entity.Category import Category
import psycopg2

class ListCategory:

    def __init__(self):
        self.connection = psycopg2.connect(
            database="Filmes",
            user='postgres',
            password='root',
            host="db",
            port=5432,
            client_encoding='utf-8'
        )

    def execute(self):
        cursor = self.connection.cursor()  
        try:
            cursor.execute("SELECT * FROM CATEGORY")
            categories = cursor.fetchall()
            return categories
        finally:
            cursor.close() 


