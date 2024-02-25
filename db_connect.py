from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs


db = input()
db_session.global_init(f'db/{db}')

db_sess = db_session.create_session()


db = input()
global_init(db)

db_sess = create_session()
for job in db_sess.query(Jobs).filter(Jobs.is_finished.is_(False), Jobs.work_size < 20):
    print(job)