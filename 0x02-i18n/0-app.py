#!/usr/bin/python3
"""basic flask app with a single route"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('0-index.html')
