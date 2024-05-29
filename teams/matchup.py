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

write_json('Angel City FC','Angel City FC','teams/AngelCityMatches.json')
write_json('Bay FC','Bay FC','teams/BayFCMatches.json')
write_json('Chicago Red Stars','Chicago Red Stars','teams/ChicagoMatches.json')
write_json('Houston Dash','Houston Dash','teams/HoustonMatches.json')
write_json('Kansas City Current','Kansas City Current','teams/CurrentMatches.json')
write_json('NJ/NY Gotham FC','NJ/NY Gotham FC','teams/GothamMatches.json')
write_json('North Carolina Courage','North Carolina Courage','teams/CourgeMatches.json')
write_json('Orlando Pride','Orlando Pride','teams/OrlandoMatches.json')
write_json('Portland Thorns FC','Portland Thorns FC','teams/PortlandMatches.json')
write_json('Racing Louisville FC','Racing Louisville FC','teams/RachingMatches.json')
write_json('San Diego Wave FC','San Diego Wave FC','teams/WaveMatches.json')
write_json('Seattle Reign','Seattle Reign','teams/SeattleMatches.json')
write_json('Utah Royals FC','Utah Royals FC','teams/UtahMatches.json')
write_json('Washington Spirit','Washington Spirit','teams/WashingtonMatches.json')
write_elo_json('Angel City FC','teams/AngelCityElo.json')
write_elo_json('Bay FC','teams/BayFCElo.json')
write_elo_json('Chicago Red Stars','teams/ChicagoElo.json')
write_elo_json('Houston Dash','teams/HoustonElo.json')
write_elo_json('Kansas City Current','teams/CurrentElo.json')
write_elo_json('NJ/NY Gotham FC','teams/GothamElo.json')
write_elo_json('North Carolina Courage','teams/CourgeElo.json')
write_elo_json('Orlando Pride','teams/OrlandoElo.json')
write_elo_json('Portland Thorns FC','teams/PortlandElo.json')
write_elo_json('Racing Louisville FC','teams/RachingElo.json')
write_elo_json('San Diego Wave FC','teams/WaveElo.json')
write_elo_json('Seattle Reign','teams/SeattleElo.json')
write_elo_json('Utah Royals FC','teams/UtahElo.json')
write_elo_json('Washington Spirit','teams/WashingtonElo.json')
