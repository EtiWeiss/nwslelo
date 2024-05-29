import mysql.connector
import json

def write_json(team1,team2,match):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="iTTia1!Rd",
        database="nwslelo"
    )
    cursor = conn.cursor()
    query = "select * from matchups where team1 = %s or team2 = %s"
    cursor.execute(query, (team1,team2))
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append(dict(zip(cursor.column_names,row)))
    with open(match,'w') as f:
        json.dump(data,f,indent=4)
    conn.close()

def write_elo_json(team1,team2):
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
    with open(team2,'w') as f:
        json.dump(data,f,indent=4)
    conn.close()

write_json('Angel City FC','Angel City FC',"teams/AngelCityMatches.json")
write_elo_json('Angel City FC',"teams/AngelCityElo.json")
write_json('Bay FC','Bay FC',"teams/BayFCMatches.json")
write_elo_json('Bay FC',"teams/BayFCElo.json")
write_json('NJ/NY Gotham FC','NJ/NY Gotham FC',"teams/GothamMatches.json")
write_elo_json('NJ/NY Gotham FC',"teams/GothamElo.json")
