import os
import hmac
import json
import logging
import subprocess
import requests
from ipaddress import ip_address, ip_network
from hashlib import sha1
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
        source_ip = ip_address('{}'.format(request.remote_addr))
        whitelist = requests.get('https://api.github.com/meta').json()['hooks']
        ip_flag = False
        for ip in whitelist:
            if source_ip in ip_network(ip):
                ip_flag = True
                break
        if not ip_flag:
            return "sorry"

        secret = os.environb[b'WEBHOOK_SECRET']
        header_signature = request.headers.get('X-Hub-Signature')
        if not header_signature:
            return "sorry"

        sha_type, signature = header_signature.split('=')
        mac = hmac.new(secret, msg=request.data, digestmod=sha1)
        if not hmac.compare_digest(mac.hexdigest(), signature):
            return "cheating"

        subprocess.call('/runhook.sh')
    return "done"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
