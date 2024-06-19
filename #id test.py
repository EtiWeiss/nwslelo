#id test
import mysql.connector
import json
def get_id():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="iTTia1!Rd",
        database="nwslelo"
    )
    cursor = conn.cursor()
    query = "SELECT MAX(id) FROM nwslelo.matchups"
    cursor.execute(query,)
    id = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return id
result = get_id()

print(f"{result}")