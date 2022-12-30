import sqlite3

class BotDB:

    def __init__(self, db_file):
        """Start connection to Database"""
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, telegram_id):
        """Сheck user in db"""
        result = self.cursor.execute("SELECT telegram_id FROM user WHERE telegram_id = ?", (telegram_id,))
        return bool(len(result.fetchall()))

    def get_user(self, telegram_id):
        """Getting user"""
        result = self.cursor.execute("SELECT 'telegram_id', 'name', 'join_date' FROM 'user' WHERE 'telegram_id' = ?", (telegram_id,))
        return result.fetchall()[0]

    def add_user(self, telegram_id, name, join_date):
        """Add user"""
        self.cursor.execute("INSERT INTO user (telegram_id, name, join_date) VALUES (?, ?, ?)", (telegram_id, name, join_date))
        return self.conn.commit()

    def count_users(self):
        users = self.cursor.execute("SELECT * FROM 'user'")
        return len(users.fetchall())

    def new_func(self, telegram_id, name, new_func):
        self.cursor.execute("INSERT INTO func (telegram_id, name, new_func) VALUES (?, ?, ?)", (telegram_id, name, new_func))
        return self.conn.commit()

    def all_news(self):
        new_func = self.cursor.execute("SELECT * FROM 'func'")
        return new_func.fetchall()

    def all_db(self):
        users = self.cursor.execute("SELECT * FROM 'user'")
        return users.fetchall()

    def close(self):
        """Close connect db"""
        self.conn.close()











