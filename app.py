from flask import Flask, render_template, request, redirect, url_for
from Code.markov_ngram import *
import re
import os


app = Flask(__name__)


@app.route('/')
def index():
    markov = Markov('Code/tweetgen.txt').n_markov
    return render_template('index.html', markov=markov)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
