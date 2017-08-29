from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/perfil/<string:username>")
def profile(username):
	url = "https://api.github.com/users/" + username + "?access_token=84f891bd9791a7bb6645ab90b8ade08dac8531da"
	r = requests.get(url)
	if r.status_code == 200:
		return render_template("profile.html", usuario=r.json())
	else:
		return abort(404)

if __name__ == "__main__":
	app.run(debug=True)