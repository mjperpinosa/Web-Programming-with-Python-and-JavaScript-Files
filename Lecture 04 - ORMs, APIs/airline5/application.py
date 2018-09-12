 from flask import Flask, render_template, request
from models import *


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
	flights = Flight.quesry.all()
	return render_template("index.html", flights=flights)


@app.route("/book", methods=["POST"])
def book():
	"""Book a flight."""

	# Get from information.
	name = request.form.get("name")
	try:
		flight_id = int(request.form.get("flight_id"))
	except ValueError:
		return render_template("error.html", message="Invalid fligh number.")

	# Make sure the flight exists.
	flight = Flight.query.get(flight_id)
	if flight is None:
		return render_template("error.html", message="No such flight with that ID.")

	# Add passenger.
	flight.add_passenger(name)
	return render_template("success.html")


@app.route("/flights")
def flights():
	"""List all flights."""
	flights = Flight.query.all()
	return render_template("flights.html", flights=flights)


@app.route("/flights/<int:flight_id>")
def flight(flight_id):
	"""List details about a signle flight."""

	#Make sure flight exists.
	flight = Flight.query.get(flight_id)
	if flight is None:
		return render_template("error.html", message="No such flight.")

	# Get all passenger.
	passengers = flight.passengers
	return render_template("flight.html", flight=flight, passengers=passengers )


app.route("/api/flights/<>")