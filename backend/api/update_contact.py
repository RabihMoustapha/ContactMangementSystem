import db

cur = db.con.cursor()

def update_firstname(contact_id, new_name):
    query = "UPDATE contact SET firstname = %s WHERE id = %s"
    cur.execute(query, (new_name, contact_id))
    db.con.commit()
    cur.close()

def update_lastname(contact_id, new_name):
    query = "UPDATE contact SET lastname = %s WHERE id = %s"
    cur.execute(query, (new_name, contact_id))
    db.con.commit()
    cur.close()

def update_country(contact_id, new_country):
    query = "UPDATE contact SET country = %s WHERE id = %s"
    cur.execute(query, (new_country, contact_id))
    db.con.commit()
    cur.close()

cur.close()
db.con.close()