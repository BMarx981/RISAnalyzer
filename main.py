#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:25:57 2019

@author: brianmarx
"""
# AU AF TI SO DT DE ID PY VL IS DI PG UT

from flask import Flask, render_template, request, send_from_directory
from RISParser import RISParser

app = Flask(__name__, static_folder='static')
rp = RISParser()
ta = ''.format('UTF-8')
fileN = None

@app.route("/")
def home():
    return render_template('home.html', ta=ta)

@app.route("/success", methods=['GET', 'POST'])
def success():
    global ta
    global fileN
    if request.method == 'POST':
        tags = str(request.form['textData']).split(' ')
        tags = [x.replace('\\n', '').replace(',', '') for x in tags]
        tags = [x.upper() for x in tags]
        tags = list(filter(None, tags))
        ta = ''
        for s in tags:
            ta += s + ' '
        f = request.files['uploadFile']
        fileN = f.filename
        content = str(f.read().decode("utf-8-sig").encode("utf-8")).split('\\n')
        content = list(filter(None, content))
        rp.processFile(content, tags, fileN)
        newShit = rp.getFileName() + '.xlsx'
        return render_template('processing.html', f=fileN, d=newShit)

@app.route("/download/<download>")
def downloadFile(download):
    
    print(download)
    return send_from_directory('static', filename=download)

if __name__ == '__main__':
    app.run(debug=True)
    
