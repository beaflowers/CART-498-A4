from flask import Flask, render_template, request
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route("/", methods=["GET", "POST"])
def index():

    result_img = None

    if request.method == "POST":
        user_prompt = request.form["prompt"]

        prompt = f"""
        {user_prompt}

        Everything should be washed out, like a watercolor painting. Not monotone but colorful.
        Some object elements such as figures, actions and settings are vivid, neon, sharp and bright. 
        Pick from one of the Jungian archtypes (Innocent, Orphan, Hero, Caregiver, Explorer, Rebel, Lover, Creator, Jester, Sage, Magician, Ruler) 
        that best suits the description, and apply some imagery from that archtype.

        Make everything very dreamlike and surreal. It should feel disorienting and wild.
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

        except Exception as e:
            return render_template("index.html", error=str(e))
        
    return render_template("index.html", result_img=result_img)

if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing