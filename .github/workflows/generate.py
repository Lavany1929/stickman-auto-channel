import os
from google import genai

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing")

client = genai.Client(api_key=api_key)

prompt = """
Create an original YouTube educational/self-improvement video
for a channel using simple black-and-white stick-figure illustrations.

Choose ONE interesting topic.

The finished video should be approximately 10-15 minutes long.

Return these sections:

TITLE:
A clickable but honest YouTube title.

SCRIPT:
Write approximately 1800-2200 words of narration.
Make it conversational, useful and entertaining.
Do not copy another creator.

SCENES:
Create approximately 35-45 scenes.

For every scene use this format:

SCENE 1
NARRATION: ...
IMAGE: ...

The IMAGE description must describe one static
black-and-white stick-figure illustration.

Keep the visual style consistent:
simple hand-drawn stick figures,
white background,
black lines,
minimal objects,
clear facial expressions,
16:9 composition.

Make the content completely original.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

if not response.text:
    raise RuntimeError("Gemini returned an empty response")

os.makedirs("output", exist_ok=True)

with open("output/script.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print("SUCCESS: script generated")
print("Characters:", len(response.text))
