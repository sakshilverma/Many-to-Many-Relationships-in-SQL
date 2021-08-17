import json
import sqlite3

con=sqlite3.connect('rdb.sqlite')
cur=con.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE
);

CREATE TABLE Course(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
title TEXT UNIQUE
);

CREATE TABLE Member(
user_id INTEGER,
course_id INTEGER,
role INTEGER,
PRIMARY KEY (user_id, course_id)
)
''')

fname=input('Enter file name - ')
if len(fname) < 1:
    fname='roster_data.json'

data=open(fname).read()
json_data=json.loads(data)

for entry in json_data:
    name=entry[0]
    title=entry[1]
    role=entry[2]
    print((name, title, role))

    cur.execute('''insert or ignore into User(name) values(?)''',(name,))
    cur.execute('''select id from User where name=?''',(name,))
    user_id=cur.fetchone()[0]

    cur.execute('''insert or ignore into Course(title) values(?)''',(title,))
    cur.execute('select id from Course where title=?',(title,))
    course_id=cur.fetchone()[0]

    cur.execute('''insert or replace into Member(user_id, course_id,
    role) values(?,?,?)''',(user_id, course_id, role))

    con.commit()
