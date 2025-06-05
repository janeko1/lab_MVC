from flask import Blueprint, request, redirect, url_for, render_template
from models.reservation import Reservation
from database.database import session

reservation_bp = Blueprint('reservation', __name__)

@reservation_bp.route('/list_reservations', methods=['GET'])
def list_reservations():
    reservations = session.query(Reservation).all()
    return render_template('reservations_list.html', reservations=reservations)

@reservation_bp.route('/reservation_form/<int:trip_id>', methods=['GET'])
def reservation_form(trip_id):
    return render_template('reservation_form.html', trip_id=trip_id)

@reservation_bp.route('/add_reservation/<int:trip_id>', methods=['POST'])
def add_reservation(trip_id):
    user_name = request.form['user_name']
    type = request.form['type']

    new_reservation = Reservation(user_name=user_name, type=type, trip_id=trip_id)
    session.add(new_reservation)
    session.commit()

    return redirect(url_for('trip.list_trips'))

@reservation_bp.route('/delete_reservation/<int:reservation_id>', methods=['POST'])
def delete_reservation(reservation_id):
    reservation = session.query(Reservation).get(reservation_id)
    if reservation:
        session.delete(reservation)
        session.commit()
        return redirect(url_for('reservation.list_reservations'))
    else:
        return "Rezerwacja nie istnieje", 404
