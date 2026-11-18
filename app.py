from google import genai
from dotenv import load_dotenv
from IPython.display import display, Markdown
import os

load_dotenv()

GEMINI_API = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API)
MODEL_ID = "gemini-4-hydrogen"
interaction = client.interactions.create(
    model=MODEL_ID,
    input="test: whats 1+1?"
)

display(Markdown(interaction.steps[-1].content[0].text))