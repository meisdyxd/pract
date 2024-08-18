import sqlite3


class DataBase:
    def __init__(self):
        self.db = sqlite3.connect("DATABASE.db")
        self.cur = self.db.cursor()
        self.createOrLoad()

    def createOrLoad(self):
        # CREATE ROUTS
        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS Routs (
                id INTEGER PRIMARY KEY,
                code_rout INTEGER UNIQUE,
                name TEXT,
                fareway INTEGER,
                timeinway INTEGER,
                payment REAL)
                """)
        # CREATE DRIVERS
        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS Drivers (
                id INTEGER PRIMARY KEY,
                code_driver INTEGER UNIQUE,
                surname TEXT,
                name TEXT,
                patronymic TEXT,
                seniority INTEGER)
                """)
        # CREATE DONEWORK
        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS DoneWork (
                id INTEGER PRIMARY KEY,
                code_rout INTEGER,
                code_driver INTEGER,
                date_shipment TEXT,
                date_return TEXT,
                payment REAL)
                """)
