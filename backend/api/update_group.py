import db

cur = db.con.cursor()

def update_group_name(group_id, new_name):
    query = "UPDATE group SET name = %s WHERE id = %s"
    cur.execute(query, (new_name, group_id))
    db.con.commit()
    cur.close()

def update_group_description(group_id, new_description):
    query = "UPDATE group SET description = %s WHERE id = %s"
    cur.execute(query, (new_description, group_id))
    db.con.commit()
    cur.close()

def update_group_members(group_id, new_members):
    query = "UPDATE group SET members = %s WHERE id = %s"
    cur.execute(query, (new_members, group_id))
    db.con.commit()
    cur.close()

cur.close()
db.con.close()