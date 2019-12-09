from flask import Flask, render_template, request, redirect, url_for
from Code.markov_ngram import *
import re
import os


app = Flask(__name__)


@app.route('/')
def index():
    ngram_markov = Markov('Code/tweetgen.txt').n_markov
    return render_template('index.html', ngram_markov=ngram_markov)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
