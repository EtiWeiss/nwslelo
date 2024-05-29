import mysql.connector
import json

def write_elo_json(team1):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="iTTia1!Rd",
        database="nwslelo"
    )
    cursor = conn.cursor()
    query = "SELECT team,elo FROM teams WHERE team = %s"
    cursor.execute(query, (team1,))
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append(dict(zip(cursor.column_names,row)))
    with open('teams/page.json','w') as f:
        json.dump(data,f,indent=4)
    conn.close()

team1 = 'Bay FC'
write_elo_json(team1)
