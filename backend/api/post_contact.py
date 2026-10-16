import db

cur = db.con.cursor()

def post_contact(firstname, lastname, country):
    query = "INSERT INTO contact (firstname, lastname, country) VALUES (%s, %s, %s)"
    cur.execute(query, (firstname, lastname, country))
    db.con.commit()
    cur.close()

cur.close()
db.con.close()