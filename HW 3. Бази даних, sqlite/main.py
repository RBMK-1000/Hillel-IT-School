from flask import Flask, request
import sqlite3
from utils import commit_sql

app = Flask(__name__)

@app.route('/phones/create_table')
def create_table() -> None:
    con = sqlite3.connect('phones.db')
    cur = con.cursor()

    sql = """
        CREATE TABLE IF NOT EXISTS Phones (
        phoneId INTEGER PRIMARY KEY,
        contactName varchar(255),
        phoneValue varchar(255)
        );
        """
    cur.execute(sql)

    con.commit()
    con.close()

    return 'create_table'


@app.route('/phones/create')
def phone_create():
    # contact_Value = request.args.get('contact', 'a')
    phone_Value = request.args.get('phoneValue', 'a')

    sql = f'''
        INSERT INTO Phones (phoneValue)
        VALUES ({phone_Value});
    '''
    commit_sql(sql)

    return 'phone_create'


@app.route('/phones/read')
def phone_read():
    connection = sqlite3.connect('phones.db')
    cur = connection.cursor()

    sql_request = '''
        SELECT * FROM Phones;
    '''
    cur.execute(sql_request)

    result = cur.fetchall()
    connection.close()

    return result


@app.route('/phones/update')
def phone_update():
    phone_value = request.args['phoneValue']
    phone_id = request.args['phoneId']

    sql = f"""
        UPDATE Phones
        SET phoneValue = "{phone_value}"
        WHERE phoneId = {phone_id};
        """
    commit_sql(sql)

    return 'phone_update'


@app.route('/phones/delete')
def phone_delete():
    phone_id = request.args['phoneId']

    sql = f"""
    DELETE FROM Phones
    WHERE phoneId = {phone_id};
    """
    commit_sql(sql)

    return 'phone_delete'


if __name__ == '__main__':
    app.run(host='0.0.0.0')