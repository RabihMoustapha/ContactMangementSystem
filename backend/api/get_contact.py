import db

cur = db.con.cursor()

def get_contact(contact_id):
    query = "SELECT * FROM contact WHERE id = %s"
    cur.execute(query, (contact_id,))
    contact = cur.fetchone()
    cur.close()
    return contact

def get_all_contacts():
    query = "SELECT * FROM contact"
    cur.execute(query)
    contacts = cur.fetchall()
    cur.close()
    return contacts

cur.close()
db.con.close()