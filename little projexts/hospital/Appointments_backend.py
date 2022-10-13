import sqlite3


class Connection:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXIST appointment('
                         'id INTEGER PRIMARY KEY, name TEXT, date REAL, note TEXT)')
        self.conn.commit()

    def append(self, name, date, note):
        self.cur.execute('INSERT INTO appointment VALUES(NULL, ?,?,?)', (name, date, note))
        self.conn.commit()

