import sqlite3

from test import list_

conn = sqlite3.connect('database_site.db')

cur = conn.cursor()
for i in list_:
    cur.execute("INSERT INTO step_test (departure_city, type_auto, type_cargo, premayment, currency) VALUES (?, ?, ?, ?, ?)", i)

conn.commit()
conn.close()