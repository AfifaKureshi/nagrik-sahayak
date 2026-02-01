import os
import google.generativeai as genai
from PIL import Image

# Create Gemini client# ---------------- GEMINI CLIENT ----------------
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def classify_issue(image_np):
    """
    Classifies the civic issue in the image.
    Returns one of:
    Pothole / Garbage / Street Light / Other
    """

    # Convert numpy array to PIL Image
    image = Image.fromarray(image_np)

    prompt = """
    You are an AI vision system for classifying civic infrastructure problems.

FIRST, carefully inspect the ROAD SURFACE.

A "Pothole" includes:
- holes or depressions in the road
- cracked or broken asphalt or concrete
- uneven road surfaces
- cavities filled with water on roads

Other categories:
- Garbage: visible trash, waste piles, dumping on streets or roadsides
- Street Light: broken, bent, damaged, fallen, or non-working street lights
- Other: if none of the above clearly apply

IMPORTANT:
- If road damage is visible, ALWAYS choose "Pothole".
- Do not confuse shadows or markings with potholes unless road damage is visible.

Choose ONLY ONE category from below and respond with ONLY the category name:
- Pothole
- Garbage
- Street Light
- Other

    """

    response = model.generate_content([prompt, image])

    return response.text.strip()

