import psycopg2

con = psycopg2.connect(
    host = "localhost",
    database = "NFA035",
    user = "postgres",
    password = ""
)

con.close()