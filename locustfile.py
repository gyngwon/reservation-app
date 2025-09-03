from locust import HttpUser, task, between
import random
import uuid

class ReservationUser(HttpUser):
    wait_time = between(1, 3)  # wait between 1–3 seconds before next task

    @task(2)
    def view_shows(self):
        """
        Fetch the list of shows (GET /shows).
        Weight = 2 → executed more frequently.
        """
        self.client.get("/shows")

    @task(1)
    def make_booking(self):
        """
        Create a booking (POST /bookings).
        Uses a random show_id from a predefined list.
        """
        # Replace with actual show IDs from your database
        available_shows = [
            "219a07ca-be06-4e45-b6e7-b772fb9f8843",  # example
            "4770f2c3-0f0d-49a5-96dd-e0a56532a6f7",  # example
        ]

        if available_shows:
            show_id = random.choice(available_shows)
        else:
            # If no shows are available, send a random UUID (will likely fail)
            show_id = str(uuid.uuid4())

        self.client.post(
            "/bookings",
            json={"show_id": show_id}
        )
