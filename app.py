from flask import Flask, jsonify, render_template
from usgs import printResults
import random

app = Flask(__name__)
disaster = printResults()
lenght = len(disaster)
@app.route('/disaster')
def serve_funny_qoutes():
	return render_template('disaster.html', output=disaster, lenght=lenght)


if __name__ == "__main__":
	app.run(debug=True)