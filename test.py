import mysql.connector
import json

#x = '{"team1" : "5","team2" : "10","points1" : 0,"points2" : 1}'
#y = json.loads(x)
#print(y["points2"])

#with open('score.json') as json_file:
#    data = json.load(json_file)

#print(data)
def write_json():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="iTTia1!Rd",
        database="nwslelo"
    )
    cursor = conn.cursor()
    query = "select team,elo from teams order by elo desc"
    cursor.execute(query)
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append(dict(zip(cursor.column_names,row)))
    with open('output.json','w') as f:
        json.dump(data,f,indent=4)
    conn.close()

write_json()
with open('output.json') as json_file:
    test = json.load(json_file)

print(test)