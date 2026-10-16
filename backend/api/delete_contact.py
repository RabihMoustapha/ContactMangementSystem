import db

cur = db.con.cursor()

def delete_contact(contact_id):
    cur = db.con.cursor()
    query = "DELETE FROM contact WHERE id = %s"
    cur.execute(query, (contact_id,))
    db.con.commit()
    cur.close()

cur.close()
db.con.close()