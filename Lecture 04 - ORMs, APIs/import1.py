import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
	f = open("flights.csv")
	reader = csv.reader(f)
	for origin, destination, duration in reader:
		flight = Flight(origin=origin, destination=destination, duration=duration)
		db.session.add(flight)
		print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
		
	db.session.commit()

if __name__ == "__main__":
	with app.app_context():
		main()