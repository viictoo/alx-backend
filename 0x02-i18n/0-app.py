#!/usr/bin/env python3
"""basic flask app with a single route"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def root():
    """root url that prints hello"""
    return render_template('0-index.html')
