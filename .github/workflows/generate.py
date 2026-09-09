import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

prompt = """
You are writing for an original YouTube channel that uses simple
black-and-white stick-figure illustrations.

Create ONE original 10-15 minute educational/self-improvement video.

Choose a useful topic with broad appeal.

Return:
1. A catchy YouTube title
2. A 10-15 minute narration script
3. A scene list with approximately 30-40 static scenes

For every scene provide:
- scene number
- short narration
- image description

Do NOT copy any existing YouTube creator.
Make the content original, useful and entertaining.

Format the answer clearly.
"""

response = client.models.generate_content(
    model="gemini-3.7-flash",
    contents=prompt
)

os.makedirs("output", exist_ok=True)

with open("output/script.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Script generated successfully!")
