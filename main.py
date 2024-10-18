from connector import Connection

passwd = "xoWsa8-pymfij-dawryn"
conn = Connection(passwd)
print(conn.msg)

query = """
    SELECT * FROM actividad;
"""

print(conn.run_query(query))
