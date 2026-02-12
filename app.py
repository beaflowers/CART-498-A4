from flask import Flask, render_template, request
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def _response_text(resp):
    if hasattr(resp, "output_text") and resp.output_text:
        return resp.output_text
    try:
        return resp.output[0].content[0].text
    except Exception:
        return ""

@app.route("/", methods=["GET", "POST"])
def index():

    result_img = None
    analysis_text = None

    if request.method == "POST":
        user_prompt = request.form["prompt"]

        prompt = f"""
        {user_prompt}

        Use a visual style that is washed out, like a watercolor painting. Not monotone, somewhat colorful, soft and flowing.
        Some object elements such as figures and nouns should be vivid, neon, and bright, with sharp edges. 

        Incorporate Jungian archtypes into the image as their own elements: 
        - Shadow figures lurking behind main characters, partially obscured by mist or darkness.
        - Mirrors reflecting distorted, warped versions of objects or characters, creating a sense of duality.
        - Circular patterns or mandalas subtly appearing in the background to represent the Self.

        Add dreamlike distortions such as warped perspectives, impossible angles, and twisting landscapes 
        and surreal lighting: soft glows, mist, shafts of light, and muted shadows creating an uncanny atmosphere.
        If relevant to the dream description, add symbolic objects: clocks, keys, stairs, doors, candles, or stairways leading nowhere.
        Composition should feel disorienting, layered, and wild.

        """

        try:
            response_img = client.images.generate(
                model="gpt-image-1-mini",  
                prompt=prompt,
                size="auto",
                moderation="low",
                quality="low",
                n=1
            )

            result_img = response_img.data[0].b64_json
            analysis_response = client.responses.create(
                model="gpt-4.1-mini",
                input=[
                    {"role": "system", "content": "You are a Jungian dream analyst. Give a concise analysis (4-6 sentences) in plain language."},
                    {"role": "user", "content": user_prompt},
                ],
                max_output_tokens=220,
            )
            analysis_text = _response_text(analysis_response).strip()

        except Exception as e:
            return render_template("index.html", error=str(e))
        
    return render_template("index.html", result_img=result_img, analysis_text=analysis_text)

if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing
