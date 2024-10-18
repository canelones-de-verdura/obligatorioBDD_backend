import connector
from connector import Consultor

passwd = "xoWsa8-pymfij-dawryn"
conn = Consultor(passwd)
print(conn.msg)

query = """
    SELECT * FROM actividad;
"""

print(conn.run_query(query))