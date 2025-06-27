class Generator:
    def __init__(self, client):
        self.client = client

    def generate_flight(self):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Return a JSON 'Flight' with flight_id, origin_airport, destination_airport, departure_time, free_seats"
        )
        return response.text