#get current elo
import mysql.connector

def get_elo(team):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="iTTia1!Rd",
        database="teams"
    )
    cursor = conn.cursor()
    query = "SELECT elo FROM nwslelo.teams WHERE team = %s"
    cursor.execute(query, (team,))
    elo = cursor.fetchone()[3]  # Assuming score is in the first column
    cursor.close()
    conn.close()
    return elo
#get score
#run calc
#update elo