from google import genai 
from google.genai import types
import os
from dotenv import load_dotenv


load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(model="gemini-2.5-flash")
def generate_response(query):
    result = chat.send_message(query)
    # for message in chat.get_history():
    #     print(f'role - {message.role}',end=": ")
    #     print(message.parts[0].text)
    return result.candidates[0].content.parts[0].text


def evaluate_response(query: str, answer: str):
    evaluation_prompt =  f"""
    Evaluate the Evaluator's answer.

    USER QUESTION:
    {query}

    ASSISTANT ANSWER:
    {answer}

    Return ONLY valid JSON with:
    - score: integer 1-10
    - feedback: short string
    """

    evaluation = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=evaluation_prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "score": types.Schema(type=types.Type.INTEGER),
                    "feedback": types.Schema(type=types.Type.STRING),
                },
                required=["score", "feedback"]
            )
        )
    )
    return evaluation.candidates[0].content.parts[0].text