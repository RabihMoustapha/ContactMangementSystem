import db

cur = db.con.cursor()

def post_group(name, description, members):
    query = "INSERT INTO group (name, description, members) VALUES (%s, %s, %s)"
    cur.execute(query, (name, description, members))
    db.con.commit()
    cur.close()

cur.close()
db.con.close()