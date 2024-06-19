#get current elo
import mysql.connector
import json

def get_elo(team):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="iTTia1!Rd",
        database="nwslelo"
    )
    cursor = conn.cursor()
    query = "SELECT elo FROM nwslelo.teams WHERE team = %s"
    cursor.execute(query, (team,))
    elo = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return elo

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

def update_elo(elo, team):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="iTTia1!Rd",
        database="nwslelo"
    )
    cursor = conn.cursor()
    query = "UPDATE nwslelo.teams SET elo = %s WHERE team = %s"
    cursor.execute(query, (elo, team))
    conn.commit()
    cursor.close()
    conn.close()

def update_matchups(id,Team1,ELO1,Team2,Elo2,Result1,Result2,Elo1new,Elo2new):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="iTTia1!Rd",
        database="nwslelo"
    )
    cursor = conn.cursor()
    query = "INSERT INTO nwslelo.matchups VALUE(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query, (id,Team1,ELO1,Team2,Elo2,Result1,Result2,Elo1new,Elo2new))
    conn.commit()
    cursor.close()
    conn.close()

def write_json():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="iTTia1!Rd",
        database="nwslelo"
    )
    cursor = conn.cursor()
    query = "select * from teams order by elo desc"
    cursor.execute(query)
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append(dict(zip(cursor.column_names,row)))
    with open('output.json','w') as f:
        json.dump(data,f,indent=4)
    conn.close()


team1 = input('Who was the first team? ')
elo_not1 = get_elo(team1)
team2 = input('Who was the second team? ')
elo_not2 = get_elo(team2)
print(f"The current elo for {team1} is {elo_not1} and {team2} is {elo_not2}")

#get score
result1 = float(input('What was the outcome? Enter 0 for the first team losing, 1 for first team winning, or 0.5 for a draw: '))
result2 = 1 - result1
if result1 > result2:
    print(f'{team1} beat {team2}')
elif result2 > result1:
    print(f'{team2} beat {team1}')
else:
    print(f'{team1} and {team2} drew')

#run calc
Qa = 10**(elo_not1/400)
Qb = 10**(elo_not2/400)
Ea = Qa/(Qa+Qb)
Eb = Qb/(Qa+Qb)
elo1new = int(elo_not1 + (32*(result1 - Ea)))
elo2new = int(elo_not2 + (32*(result2 - Eb)))
print(f"The new elo for {team1} is {elo1new} and {team2} is {elo2new}")
commit = input('Is this correct? Y/N: ')

if commit == 'Y':
    update_elo(elo1new,team1) #update elo
    update_elo(elo2new,team2) #update elo
    id = get_id() + 1
    update_matchups(id,team1,elo_not1,team2,elo_not2,result1,result2,elo1new,elo2new) #update matchup
    write_json() #outputs to json file, picked up by js to html
    print('Elo has been updated!')
else:
    print('Start program again and enter correct info. If problem persists, contact Support')

