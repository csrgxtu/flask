import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from flask import Flask, session
import json


app = Flask(__name__)


@app.route('/user_info')
def user_info():
	if 'user_info' not in session:
		return 'not in session'

	user_info = session['user_info']
	return json.dumps(user_info, indent=2)


@app.route('/login/<username>')
def login(username):
	session['user_info'] = {
		'username': username,
		'avatar': 'http://t.com/7yf32f.jpg'
	}
	return '{} logged in'.format(username)


@app.route('/logout')
def logout():
	user_info = session.pop('user_info')
	return '{} logged out'.format(user_info['username'])


# secret_key
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == '__main__':
	app.run()
