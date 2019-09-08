from flask import Flask, jsonify, render_template, redirect, url_for, request, flash
from usgs import printResults

app = Flask(__name__)

@app.route('/disaster', methods =('GET', 'POST'))
def serve_funny_qoutes():
	magnitude = 1
	if request.method == 'POST':
    		magnitude = request.form.get('magnitude', type=float)

	disaster = printResults(magnitude)
	lenght = len(disaster)

	return render_template('disaster.html', output=disaster, lenght=lenght)



if __name__ == "__main__":
	app.run(debug=True)