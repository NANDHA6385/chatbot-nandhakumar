from pymongo import MonogoClient
try:
    conn=MonogoClient()
    print("connected successfully!!!")
except:
    print("could not connect to MongoDB")
    db=conn.mydatabase
    collection=db.mytable
    cursor=collection.find()
    for record in cursor:
        print(record)