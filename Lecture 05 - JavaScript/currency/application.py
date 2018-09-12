
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():

	# Query for currency exchange rate
	currency = request.form.get("currency")
	res = requests.get("http://api.fixer.io/latest", params={
		"base": "USD", "symbols": currency })


	# Make sure request succeeded
	if res.status_code != 200:
		return jsonify({"succss": False})


	# Make sure currency is in response
	data = res.json()
	if currency not in data["rates"]:
		return jsonify({"success": False})

	return jsonify({"success": True, "rate": data["rates"][currency]})