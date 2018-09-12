SELECT * FROM flights JOIN passengers
	ON flights.id = passengers.flight_id
	WHERE passengers.name = 'Alice';

/* Passenger.query.filter_by(name="Alice).first().flight" */