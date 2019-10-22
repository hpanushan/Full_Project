import os
import subprocess

def buildAndMoveFiles():
    CURRENT_DIRECTORY = os.getcwd()
    PROJECT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

    FLASK_STATIC_PATH = os.path.join(PROJECT_DIRECTORY, 'static')
    FLASK_TEMPLATES_PATH = os.path.join(PROJECT_DIRECTORY, 'templates')

    subprocess.run(('cd ' + CURRENT_DIRECTORY + ' && ng build --base-href /static/'), shell=True)

    DIST_PATH = CURRENT_DIRECTORY + '\dist'

    try:
        subprocess.call(('cd ' + DIST_PATH + ' &&' + ' cd angular &&' + ' move ' + '"main.js"' + ' "' + FLASK_STATIC_PATH + '"'),shell=True)
        subprocess.call(('cd ' + DIST_PATH + ' &&' + ' cd angular &&' + ' move ' + '"main.js.map"' + ' "' + FLASK_STATIC_PATH + '"'), shell=True)
        subprocess.call(('cd ' + DIST_PATH + ' &&' + ' cd angular &&' + ' move ' + '"polyfills.js"' + ' "' + FLASK_STATIC_PATH + '"'),shell=True)
        subprocess.call(('cd ' + DIST_PATH + ' &&' + ' cd angular &&' + ' move ' + '"polyfills.js.map"' + ' "' + FLASK_STATIC_PATH + '"'),shell=True)
        subprocess.call(('cd ' + DIST_PATH + ' &&' + ' cd angular &&' + ' move ' + '"polyfills-es5.js"' + ' "' + FLASK_STATIC_PATH + '"'),shell=True)
        subprocess.call(('cd ' + DIST_PATH + ' &&' + ' cd angular &&' + ' move ' + '"polyfills-es5.js.map"' + ' "' + FLASK_STATIC_PATH + '"'),shell=True)
        subprocess.call(('cd ' + DIST_PATH + ' &&' + ' cd angular &&' + ' move ' + '"runtime.js"' + ' "' + FLASK_STATIC_PATH + '"'),shell=True)
        subprocess.call(('cd ' + DIST_PATH + ' &&' + ' cd angular &&' + ' move ' + '"runtime.js.map"' + ' "' + FLASK_STATIC_PATH + '"'),shell=True)
        subprocess.call(('cd ' + DIST_PATH + ' &&' + ' cd angular &&' + ' move ' + '"styles.js"' + ' "' + FLASK_STATIC_PATH + '"'),shell=True)
        subprocess.call(('cd ' + DIST_PATH + ' &&' + ' cd angular &&' + ' move ' + '"styles.js.map"' + ' "' + FLASK_STATIC_PATH + '"'),shell=True)
        subprocess.call(('cd ' + DIST_PATH + ' &&' + ' cd angular &&' + ' move ' + '"vendor.js"' + ' "' + FLASK_STATIC_PATH + '"'),shell=True)
        subprocess.call(('cd ' + DIST_PATH + ' &&' + ' cd angular &&' + ' move ' + '"vendor.js.map"' + ' "' + FLASK_STATIC_PATH + '"'),shell=True)

        subprocess.call(('cd ' + DIST_PATH + ' &&' + ' cd angular &&' + ' move ' + '"index.html"' + ' "' + FLASK_TEMPLATES_PATH + '"'), shell=True)

    except Exception as e:
        dir_exists = False
        print(e)

buildAndMoveFiles()
