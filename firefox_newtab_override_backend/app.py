#!/usr/bin/env python3

# https://addons.mozilla.org/en-US/firefox/addon/new-tab-override/
# Can't do JS magic with local files. Just serve it from srv ¯\_(ツ)_/¯

from pprint import pprint as pp
from flask import *
app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('ahhh.html')



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=3000)
