from fastapi import FastAPI
from fastapi.responses import JSONResponse
from generator import Generator
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()
app = FastAPI()
generator = Generator(client)

@app.get("/")
async def root():
    return JSONResponse(content=generator.generate_flight(), media_type="application/json")
