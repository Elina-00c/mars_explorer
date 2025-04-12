from flask import Flask
from data.users import User
from data.jobs import Jobs
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    app.run()


if __name__ == '__main__':
    main()

user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"

db_sess = db_session.create_session()
db_sess.add(user)

user = User()
user.surname = "Waters"
user.name = "Lowell"
user.age = 23
user.position = "engineer"
user.speciality = "mechanical"
user.address = "module_2"
user.email = "waters_mechanical@mars.org"

db_sess.add(user)

user = User()
user.surname = "Armstrong"
user.name = "Sylvia"
user.age = 25
user.position = "pilot"
user.speciality = "spacecraft pilot"
user.address = "module_3"
user.email = "sylvia_pilot@mars.org"

db_sess.add(user)

user = User()
user.surname = "Johnson"
user.name = "Emily"
user.age = 30
user.position = "scientist"
user.speciality = "astronomy scientist"
user.address = "module_4"
user.email = "johnson_scientist@mars.org"

db_sess.add(user)

jobs = Jobs()
jobs.team_leader = 1
jobs.job = "deployment of residential modules 1 and 2"
jobs.work_size = 15
jobs.collaborators = "2, 3"
jobs.is_finished = False

db_sess.add(jobs)
db_sess.commit()
