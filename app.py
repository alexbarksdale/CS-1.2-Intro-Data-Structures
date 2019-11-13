from flask import Flask, render_template, request, redirect, url_for
from Code.histogram import histogram_dict
from Code.sample import sample_freq
import os


app = Flask(__name__)

#! Note: Focusing on the data structures before web


@app.route('/')
def index():

    source_file = 'Code/sampletest.txt'
    with open(source_file, 'r') as source:
        source_file = source.read().split()

    histo = histogram_dict(source_file)
    sample = sample_freq(histo)

    return render_template('index.html', sample=sample)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
