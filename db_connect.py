from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.departments import Department


db = input()
db_session.global_init(f'db/{db}')

db_sess = db_session.create_session()

db = input()
global_init(db)

db_sess = create_session()
members = {x: 0 for x in map(int, db_sess.query(Department).first().members.split(', '))}
for job in db_sess.query(Jobs).all():
    collaborators = list(map(int, job.collaborators.split(', ')))
    for c in collaborators:
        if c in members:
            members[c] += job.work_size

users = db_sess.query(User).all()
for user in users:
    if members.get(user.id, 0) > 25:
        print(user.surname, user.name)
