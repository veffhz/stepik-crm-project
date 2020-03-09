## CRM project with Flask

##### features:
 - admin panel for manage courses
 - admin panel for manage groups
 - admin panel for manage users
 - admin dashboard for statistic
 
##### requirements:
 - Python 3.5+
 - Flask 1.1.1
 - Gunicorn 20.0.4

##### install requirements:
`pip3 install -r requirements.txt`

##### create and fill db:
`flask db upgrade`

`python migrate_to_db.py`

##### run app:
 - run `gunicorn 'wsgi:app'`
 - open default page http://127.0.0.1:8000
