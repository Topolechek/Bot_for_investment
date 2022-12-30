import sqlite3

try:
    conn = sqlite3.connect('users_log.db')
    cursor = conn.cursor()

    conn.commit()


except sqlite3.Error as error:
    print('Error', error)

finally:
    if conn:
        conn.close()