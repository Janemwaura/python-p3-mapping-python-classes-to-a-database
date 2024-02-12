import pdb
from config import CONN, CURSOR
pdb.set_trace()

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album
    @classmethod
    def create_table(self):
       sql = """CREATE TABLE IF NOT EXISTS songs(
           id INTEGER PRIMARY KEY,
           name TEXT NOT NULL,
           album TEXT NOT NULL
       )"""   

       cursor.execute(sql)
    def save(self):
        sql = """INSERT INTO songs(name, album) VALUES(?, ?)"""
        cursor.execute(sql, (self.name, self.album))
        CONN.commit()
hello = Song("Hello", "25")
hello.save()

despacito = Song("Despacito", "Vida")
despacito.save()