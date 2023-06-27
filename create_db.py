import sqlite3

conn = sqlite3.connect('database_site.db')
cur = conn.cursor()
#
# cur.execute('''CREATE TABLE step_2 (
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# departure_city TEXT,
# destination_city TEXT,
# type_auto TEXT,
# type_cargo TEXT,
# tonnage TEXT,
# stops TEXT,
# prepayment TEXT,
# currency TEXT,
# mode_transportation TEXT,
# type_load TEXT,
# data_load TEXT,
# temperature_regime TEXT,
# cargo_readiness TEXT,
# table_processing TEXT,
# _id INTEGER,
# userid INTEGER,
# data DATE,
# phone_num TEXT,
# email TEXT,
# cargo_danger TEXT)''')


# cur.execute('''CREATE TABLE step_test
#                   (departure_city TEXT, type_auto TEXT, type_cargo TEXT, premayment TEXT, currency TEXT)''')


# cur.execute('''INSERT INTO message_2(id, username, text, structuring)
# SELECT id, username, text, structuring FROM messages)''')

# #
cur.execute('''CREATE TABLE spum
                  (text_spam TEXT)''')


conn.commit()
conn.close()