import sqlite3 as sq

with sq.connect('saper.db') as con:
	cur  = con.cursor()
	cur.execute('''DROP TABLE IF EXISTS users''')
	cur.execute('''CREATE TABLE IF NOT EXISTS users (
		name TEXT,
		sex INTEGER DEFAULT 1,
		old INTEGER,
		score INTEGER DEFAULT 0
		)''')

