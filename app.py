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
        prompt = request.form["prompt"]
        try:
            response_img = client.images.generate(
                model="gpt-image-1.5",  
                prompt=prompt,
                size="auto",
                n=1
            )

            result_img = response_img.data[0].b64_json

        except Exception as e:
            return render_template("index.html", error=str(e))
        
    return render_template("index.html", result_img=result_img)

if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing