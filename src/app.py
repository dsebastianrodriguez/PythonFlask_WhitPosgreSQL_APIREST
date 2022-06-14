from flask import Flask, Blueprint, jsonify, request, session
from config import config
from flask_cors import CORS
import psycopg2
import psycopg2.extras
from database.db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash
#Routes
from routes import Employed

app = Flask(__name__)
CORS(app,resources={"*":{"oringins":"http://localhost:3000"}})

@app.route('/')
def home():
    generate_password_hash('administrador1')
    if 'username' in session:
        username = session['username']
        return jsonify({'message': 'You are already logged in', 'username': username})
    else:
        resp = jsonify({'message': 'Unauthorized'})
        resp.status_code = 401
        return resp
        
@app.route('/login', methods=['POST'])
def login():
    connection=get_connection()
    _json = request.json
    _username = _json['username']
    _password = _json['password']
    print(_password)
    if _username and _password:
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "SELECT * FROM useraccount WHERE username=%s"
        sql_where = (_username,)
        cursor.execute(sql, sql_where)
        row = cursor.fetchone()
        username = row['username']
        password = row['password']
        if row:
            if check_password_hash(password, _password):
                session['username']=username
                cursor.close()
                return jsonify({'message':'Logged succesfully'})
            else:
                resp = jsonify({'message': 'Bad Request - Invalid password'})
                resp.status_code = 400
                return resp
    else:
        resp = jsonify({'message': 'Bad Request - Invalid credentials'})
        resp.status_code = 400
        return resp

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
    return jsonify({'message': 'Logout succesfully'})

def page_not_found(error):
    return "<h1>Not found page</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    #Blueprints
    # home()
    app.register_blueprint(Employed.main,url_prefix='/api/employed')

    #error handler
    app.register_error_handler(404, page_not_found)
    app.run()
