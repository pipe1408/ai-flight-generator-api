import json

class Generator:
    def __init__(self, client):
        self.client = client

    def generate_flight(self):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=(
                "Return only a JSON object with the following structure:\n"
                "Flight: flight_id, origin_airport, destination_airport, departure_time, free_seats.\n"
                "Do not include any markdown formatting, code blocks, or text—only raw JSON."
            ),
        )

        return json.loads(response.text.strip())