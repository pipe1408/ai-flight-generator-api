from fastapi import FastAPI
from generator import Generator
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()
app = FastAPI()
generator = Generator(client)

@app.get("/")
async def root():
    return generator.generate_flight()
