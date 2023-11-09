from flask import Flask, request
import sqlite3
from utils import commit_sql

app = Flask(__name__)


# @app.route('/email/create')
# def emails_create():
#     email_value = request.args.get('email', 'a')

#     sql = f"""
#     INSERT INTO Emails (Email)
#     VALUES ({email_value});
#     """
#     commit_sql(sql)

#     return 'emails_create'


# @app.route('/email/read')
# def emails_read():
#     import sqlite3
#     con = sqlite3.connect('example.db')
#     cur = con.cursor()

#     sql = """
#     SELECT * FROM Emails;
#     """
#     cur.execute(sql)

#     result = cur.fetchall()
#     con.close()

#     return result


# @app.route('/email/update')
# def emails_update():
#     email_value = request.args['email']
#     email_id = request.args['id']

#     sql = f"""
#     UPDATE Emails
#     SET Email = '{email_value}'
#     WHERE EmailID = {email_id};
#     """
#     commit_sql(sql)

#     return 'emails_update'


# @app.route('/email/delete')
# def emails_delete():
#     email_id = request.args['id']

#     sql = f"""
#     DELETE FROM Emails
#     WHERE EmailID = {email_id};
#     """
#     commit_sql(sql)

#     return 'emails_delete'

# @app.route('/phones/delete')
# def phones_delete():


if __name__ == '__main__':
    app.run(host='0.0.0.0')