import psycopg2

try:
    connection = psycopg2.connect(
        database="Filmes",
        user='postgres',
        password='root',
        host='db',
        port='5432',
        client_encoding='utf-8'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT 1")
    print("Connection successful!")
    cursor.close()
    connection.close()
except Exception as e:
    print(f"Connection failed: {e}")
