import json
import logging
import subprocess
from pprint import pprint
from flask import Flask, request

log = logging.getLogger()
log.level = logging.INFO
fh = logging.FileHandler('./web.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
fh.setFormatter(formatter)
log.addHandler(fh)

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'



@app.route('/webhook/dgplug/', methods=['POST'])
def updatehook():
    rf = request.form
    if request.method == 'POST':
        subprocess.call('/runhook.sh')

    return "done"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
