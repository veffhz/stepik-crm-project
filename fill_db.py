import datetime

from application import create_app
from application.models import db, Group, Applicant, User, GroupCourse

applicants = [
    {
        'id': 1,
        'name': 'Ivan Restov',
        'phone': '+7(444)234-23-53',
        'email': 'app1@localhost.ru',
        'status': 'new',
        'group_id': 1,
    },
    {
        'id': 2,
        'name': 'Nikolay Destoy',
        'phone': '+7(444)334-23-53',
        'email': 'app2@localhost.ru',
        'status': 'new',
        'group_id': 2,
    },
    {
        'id': 3,
        'name': 'Oleg Mestov',
        'phone': '+7(444)434-23-53',
        'email': 'app3@localhost.ru',
        'status': 'processing',
        'group_id': 2,
    },
    {
        'id': 4,
        'name': 'Fedor Astov',
        'phone': '+7(444)534-23-53',
        'email': 'app4@localhost.ru',
        'status': 'paid',
        'group_id': 3,
    },
    {
        'id': 5,
        'name': 'Dmitriy Destov',
        'phone': '+7(444)634-23-53',
        'email': 'app5@localhost.ru',
        'status': 'distributed',
        'group_id': 4,
    },
]

groups = [
    {
        'id': 1,
        'title': 'Python Course',
        'status': 'enroll',
        'course': GroupCourse.python,
        'start': datetime.date(2020, 2, 25),
        'seats': 4,
        'applicants': [],
    },
    {
        'id': 2,
        'title': 'Vue Course',
        'status': 'enroll',
        'course': GroupCourse.vue,
        'start': datetime.date(2020, 6, 25),
        'seats': 3,
        'applicants': [],
    },
    {
        'id': 3,
        'title': 'Django Course',
        'status': 'enroll',
        'course': GroupCourse.django,
        'start': datetime.date(2020, 1, 25),
        'seats': 5,
        'applicants': [],
    },
    {
        'id': 4,
        'title': 'PHP Course',
        'status': 'enroll',
        'course': GroupCourse.php,
        'start': datetime.date(2020, 5, 25),
        'seats': 6,
        'applicants': [],
    },
    {
        'id': 5,
        'title': 'HTML Course',
        'status': 'enroll',
        'course': GroupCourse.html,
        'start': datetime.date(2020, 3, 25),
        'seats': 2,
        'applicants': [],
    },
]


def run():
    app = create_app()
    app.app_context().push()

    for applicant_dict in applicants:
        applicant = Applicant(**applicant_dict)
        db.session.add(applicant)

    db.session.commit()

    for group_dict in groups:
        group = Group(**group_dict)
        db.session.add(group)

    db.session.commit()

    user_adm = User(name='admin', email='admin@localhost.com', password='12345678')
    user = User(name='user', email='user@localhost.com', password='12345678')

    db.session.add_all([user_adm, user])
    db.session.commit()


if __name__ == "__main__":
    run()
