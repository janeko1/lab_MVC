from flask import Blueprint, render_template, request, redirect, url_for
from models.trip import Trip
from models.reservation import Reservation
from database.database import session
from datetime import datetime

trip_bp = Blueprint('trip', __name__)

@trip_bp.route('/trips', methods=['GET'])
def list_trips():
    trips = session.query(Trip).all()

    if not trips:  # Jeśli lista podróży jest pusta
        message = "Brak dostępnych podróży. Dodaj pierwszą podróż!"
    else:
        message = None  # Nie pokazuj komunikatu, jeśli są podróże
    print("Ładowanie index.html z trips:", trips)
    print("Wiadomość:", message)
    return render_template('index.html', trips=trips, message=message if message else "")

@trip_bp.route('/add_trip', methods=['GET', 'POST'])
def add_trip():
    if request.method == 'POST':
        destination = request.form['destination']
        date_str = request.form['date']

        # Konwersja stringa na obiekt date
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

        new_trip = Trip(destination=destination, date=date_obj)
        session.add(new_trip)
        session.commit()

        return redirect(url_for('trip.list_trips'))

    return render_template('trip_form.html')  # Wyświetlanie formularza dodawania podróży

@trip_bp.route('/delete_trip/<int:trip_id>', methods=['POST'])
def delete_trip(trip_id):
    trip = session.query(Trip).get(trip_id)
    if trip:
        session.delete(trip)
        session.commit()
        return redirect(url_for('trip.list_trips'))
    else:
        return "Podróż nie istnieje", 404

@trip_bp.route('/trip/<int:trip_id>', methods=['GET'])
def trip_details(trip_id):
    trip = session.query(Trip).get(trip_id)
    if trip:
        return render_template('trip_details.html', trip=trip)
    else:
        return "Podróż nie istnieje", 404
