import db

cur = db.con.cursor()

def delete_group(group_id):
    query = "DELETE FROM group WHERE id = %s"
    cur.execute(query, (group_id,))
    db.con.commit()
    cur.close()

cur.close()
db.con.close()