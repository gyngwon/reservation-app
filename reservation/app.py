from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

shows = []
bookings = []

@app.route("/shows", methods=["GET", "POST"])
def handle_shows():
    if request.method == "POST":
        data = request.json
        show = {
            "id": str(uuid.uuid4()),
            "name": data.get("name"),
            "capacity": data.get("capacity", 100),
            "available_seats": data.get("capacity", 100)
        }
        shows.append(show)
        return jsonify(show), 201
    return jsonify(shows)

@app.route("/bookings", methods=["POST"])
def create_booking():
    data = request.json
    show_id = data.get("show_id")
    for s in shows:
        if s["id"] == show_id and s["available_seats"] > 0:
            s["available_seats"] -= 1
            booking = {"id": str(uuid.uuid4()), "show_id": show_id}
            bookings.append(booking)
            return jsonify(booking), 201
    return jsonify({"error": "No seats available"}), 400

@app.route("/bookings", methods=["GET"])
def list_bookings():
    return jsonify(bookings)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
