from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Return a JSON 'Flight' with flight_id, origin_airport, destination_airport, departure_time, free_seats"
)
print(response.text)
