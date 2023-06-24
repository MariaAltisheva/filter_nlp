import sqlite3

conn = sqlite3.connect('database_site.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE step_2 (
id INTEGER PRIMARY KEY NOT NULL,
departure_city TEXT,
destination_city TEXT,
type_auto TEXT,
type_cargo TEXT,
tonnage TEXT,
stops TEXT,
prepayment TEXT,
currency TEXT,
mode_transportation TEXT,
type_load TEXT,
data_load TEXT,
temperature_regime TEXT,
cargo_readiness TEXT,
table_processing TEXT,
_id INTEGER,
userid INTEGER,
data DATE,
phone_num TEXT,
email TEXT,
cargo_danger TEXT)''')
