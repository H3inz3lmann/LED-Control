__author__ = 'matthias'

import os.path

import threading

from light_controlles import controller
import light_schemes

from bottle import route, run, template, request, static_file

manager = controller.Manager('/dev/ttyACM0', 5)
thread = None
app = None

__dir__ = os.path.dirname(__file__)
data_dir = os.path.abspath(os.path.join(__dir__, '..', 'data'))

print(data_dir)

@route('/start/<name>')
def start(name):
    global app, thread
    if thread and app:
        app.stop()
        thread.join()
    app = light_schemes.applications[name](manager)
    app.set_options(request.params)
    thread = threading.Thread(target=app.start)
    thread.start()


@route('/stop')
def stop():
    global app, thread
    if thread and app:
        app.stop()
        thread.join()
        manager.color(manager.all(), (0, 0, 0))
        app = None
        thread = None

@route('/')
def index():
    return static_file('index.html', data_dir)

run(host='', port=8080)

