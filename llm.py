import openai
from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_health_response(query):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful health assistant."},
            {"role": "user", "content": query}
        ]
    )

    return response['choices'][0]['message']['content']