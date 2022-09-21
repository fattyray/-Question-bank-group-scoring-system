import sqlite3
from exercise_num import *
def insert_db(text1:str,mt_type:int,answer:str):
    db = sqlite3.connect("exercise.db")
    curser = db.cursor()
    curser.execute(''' 
    create table if not exists exercise(
    id int primary key,
    type int not null,
    info varchar(300),
    answer varchar(30))
    ''')
    s = getinfo()
    my_id = s[0] + s[1] + s[2]
    curser.execute('''
    insert into exercise values({},{},'{}','{}');
    '''.format(my_id, mt_type, text1, answer))
    db.commit()
    addinfo(mt_type)

def get_exercises()->list:
    db = sqlite3.connect("exercise.db")
    curser = db.cursor()
    s = []
    curser.execute("select * from exercise where type=1")
    s.append(curser.fetchall())
    curser.execute("select * from exercise where type=2")
    s.append(curser.fetchall())
    curser.execute("select * from exercise where type=3")
    s.append(curser.fetchall())
    print(s)
    return s

# db = sqlite3.connect("exercise.db")
# curser = db.cursor()
# curser.execute("select * from exercise ")
# s=curser.fetchall()
# print(s)