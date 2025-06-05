from flask import Flask, redirect, url_for
from controllers.trip_controller import trip_bp
from controllers.reservation_controller import reservation_bp
from database.database import init_db

# Inicjalizacja aplikacji Flask
app = Flask(__name__)

# Rejestracja blueprintów
app.register_blueprint(trip_bp, url_prefix="/trip")
app.register_blueprint(reservation_bp, url_prefix="/reservation")

# Inicjalizacja bazy danych
init_db()

# Strona główna przekierowująca na listę podróży
@app.route("/")
def home():
    return redirect(url_for("trip.list_trips"))

if __name__ == "__main__":
    app.run(debug=True)
