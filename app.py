from flask import Flask, render_template, request, redirect, url_for
from Code.markov_ngram import *
import re
import os


app = Flask(__name__)
# Stores the markov chain
markov = Markov('Code/tweetgen.txt')


@app.route('/')
def index():
    return render_template('base.html', markov=markov)


@app.route('/generateQuote')
def generate():
    return markov.gen_ngram_markov()


if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
