#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:25:57 2019

@author: brianmarx
"""

from flask import Flask, render_template, request
from RISParser import RISParser

app = Flask(__name__)
rp = RISParser()

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/success", methods=['GET', 'POST'])
def success():
    if request.method == 'POST':
        tags = str(request.form['textData']).split(' ')
        tags = [x.replace('\\n', '').replace(',', '') for x in tags]
        tags = list(filter(None, tags))
        f = request.files['uploadFile']
        content = str(f.read().decode("utf-8-sig").encode("utf-8")).split('\\n')
        content = list(filter(None, content))
        rp.processFile(content, tags, f.filename)
        return render_template('processing.html')

if __name__ == '__main__':
    app.run(debug=True)
    
