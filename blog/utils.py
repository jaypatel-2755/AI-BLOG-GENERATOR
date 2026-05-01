import os
import re

from google.genai import Client

GEMINI_MODEL = "gemini-2.5-flash"


def clean_text(text):
    text = text.strip()
    text = re.sub(r'\r\n?', '\n', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()


def generate_blog_content(topic: str) -> str:
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise EnvironmentError("GEMINI_API_KEY is not configured in environment variables.")

    client = Client(api_key=gemini_api_key)
    prompt = f"""
Write a detailed blog article (minimum 700 words) on the topic: {topic}.

IMPORTANT RULES:

* Use simple English
* DO NOT use markdown symbols (#, ##, ###)
* Write in proper paragraphs
* Leave a blank line between each paragraph
* Each paragraph should be 4–5 lines long

Structure:

1. Title
2. Introduction (2 paragraphs)
3. 4 sections with headings (plain text only)
4. Each section must have 2 paragraphs
5. Conclusion

Make sure the content is long and well explained.
"""

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config={"temperature": 0.7, "max_output_tokens": 1500},
        )
        raw = response.text if hasattr(response, "text") else str(response)
        content = clean_text(raw)
    except Exception as e:
        content = f"Error: {str(e)}"

    return content.strip()
