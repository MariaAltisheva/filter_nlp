import sqlite3

conn = sqlite3.connect('database_site.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE message_2 AS
SELECT DISTINCT username, text, structuring 
FROM messages''')

# cur.execute('''SELECT id FROM messages GROUP BY text''')
# cur.execute('''DELETE FROM messages WHERE id NOT IN (SELECT id FROM messages GROUP BY text HAVING count(1) > 1)''')
# cur.execute('''CREATE TABLE messages_2 AS
# SELECT DISTINCT text FROM messages''')

# cur.execute('''CREATE TABLE message_2 (
# id INTEGER PRIMARY KEY,
#   username TEXT,
#   text TEXT,
#   structuring JSON
# )''')

# cur.execute('''INSERT INTO message_2(id, username, text, structuring)
# SELECT id, username, text, structuring FROM messages''')

# cur.execute('''DELETE FROM messages
# WHERE text IN (
#   SELECT text
#   FROM messages
#   GROUP BY text
#   HAVING COUNT(*) > 1
# )''')