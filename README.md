# ✈️ AI Flight Generator API

A minimal FastAPI-based example demonstrating integration with the **Gemini 2.5 Flash API (Free Tier)** to generate a JSON object with relative consistency.

---

## Usage

1. **Create a free key at [Google AI Studio](https://aistudio.google.com/apikey)**
   

2. **Clone the repository:**

   ```bash
   git clone https://github.com/pipe1408/ai-flight-generator-api.git
   cd ai-flight-generator-api
   ```

3. **Create a `.env` file with:**

   ```env
   GEMINI_API_KEY=your-api-key-here
   ```

4. **Run the API server:**

   ```bash
   fastapi dev ./main.py
   ```

5. **Access the API at [http://127.0.0.1:8000](http://127.0.0.1:8000)**

   (Reload to generate a new object)
