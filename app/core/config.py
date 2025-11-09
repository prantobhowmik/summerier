import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("OPENAI_API_BASE_URL", "https://openrouter.ai/api/v1"),
    api_key=os.getenv("OPENAI_API_KEY")
)
