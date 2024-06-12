import sqlite3
conn=sqlite3.connect('chatbot.db')
c=conn.cursor()
c.execute(''' CREATE TABLE IF NOT EXISTS user_data(
    user_id TEXT PRIMARY KEY ,
               name TEXT,
               age integer
               )
               ''')
def store_user_data(user_id,name,age):
    with conn:
        c.execute("INSERT OR REPLACE INTO user_data(user_id,name,age)VALUES(?,?,?)",
       (user_id,name,age))
        def reterive_user_data(user_id):
            c.execute("SELECT*FROM user_data WHERE user_id=?",(user_id))
            return c.fetchone()
        store_user_data("user1", "ALICE",30)
        print(reterive_user_data("user1"))
        conn.close()