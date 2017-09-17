import io
import os
import uuid
import ConfigParser
from flask import Flask
from flask import render_template
from flask import send_from_directory
from uuid import getnode as get_mac

app = Flask(__name__,static_url_path='/static')

conf_str = open("app.conf", "r").read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(conf_str))

DB_HOST = config.get("dbserver", "host")
DB_USER = config.get("dbserver", "username")
DB_PASS = config.get("dbserver", "password")

PORT = int(os.getenv('PORT', 5000))

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('./static/js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('./static/css', path)


@app.route('/')
def index():
    HOST_INFO = ""
    HOST_INFO += "Index Page<br>"
    HOST_INFO += "Database host: "+DB_HOST+"<br>"
    HOST_INFO += "Database user: "+DB_USER+"<br>"
    HOST_INFO += "Database password: "+DB_PASS+"<br>"
    HOST_INFO += "MAC ADDR of HOST: "+str(get_mac())+"<br>"
    return HOST_STR

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=PORT)
