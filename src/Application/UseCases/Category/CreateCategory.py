from src.Domain.Entity.Category import Category
import psycopg2

class CreateCategory:
    def __init__(self):
        self.connection = psycopg2.connect(
            database="Filmes",
            user='postgres',
            password='root',
            host="db",
            port=5432,
            client_encoding='utf-8'
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Category (
            id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            is_active BOOLEAN,
            created_at TIMESTAMP          
        );
        """)
        self.connection.commit()
    
    def execute(self, name, description):
        category = Category(name, description)
        try:
            self.cursor.execute("""
            INSERT INTO Category (id, name, description, is_active, created_at)
            VALUES (%s, %s, %s, %s, %s)
            """, (category.id, category.name, category.description, category.isActive, category.createdAt))
            self.connection.commit()
            return True, "Category created successfully"
        except psycopg2.Error as e:
            self.connection.rollback()
            return False, f"Error creating category: {e}"
        finally:
            self.cursor.close()
            self.connection.close()
