import db

cur = db.con.cursor()

def get_group(group_id):
    query = "SELECT * FROM group WHERE id = %s"
    cur.execute(query, (group_id,))
    group = cur.fetchone()
    cur.close()
    return group

def get_all_groups():
    query = "SELECT * FROM group"
    cur.execute(query)
    groups = cur.fetchall()
    cur.close()
    return groups

cur.close()
db.con.close()