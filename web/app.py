"""
Kalissa Concepcion's Flask API.
"""

from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route("/")
def hello():
	return "UOCIS docker demo!\n"

@app.route("/<path:filename>")
def file_checker(filename):
	if ("//" in filename) or (".." in filename) or ("~" in filename):
		abort(403)
	else:
		try:
			return render_template(filename), 200
		except:
			abort(404)

@app.errorhandler(404)
def file_not_found(e):
	return render_template("404.html"), 404

@app.errorhandler(403)
def file_forbidden(e):
	return render_template("403.html"), 403

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')

