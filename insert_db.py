import sqlite3

from test import list_, list_spam

conn = sqlite3.connect('database_site.db')

cur = conn.cursor()
# for i in list_:
#     cur.execute("""INSERT INTO step_2 (
#     id,
#     departure_city,
#     destination_city,
#     type_auto,
#     type_cargo,
#     tonnage,
#     stops,
#     prepayment,
#     currency,
#     mode_transportation,
#     type_load,
#     data_load,
#     temperature_regime,
#     cargo_readiness,
#     table_processing,
#     _id,
#     userid,
#     data,
#     phone_num,
#     email,
#     cargo_danger) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", i)


for i in list_spam:
    cur.execute(f"""INSERT INTO spum (text_spam) VALUES (?)""", i)





conn.commit()
conn.close()
# if __name__ == "__main__":