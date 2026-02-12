# Dream Machine (Flask + OpenAI Image Generation)

This is a small Flask web app that takes a user's dream description, enriches it with Jungian archetypes and visual style guidance, and generates an image using the OpenAI Images API. The UI lives in `templates/index.html`.

## Entry Point

The application entry point is `app.py` (runs a Flask server and handles the form POST).

## Quick Start

1. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install flask openai python-dotenv
```

3. Create a `.env` file at the repo root and set your API key:

```
OPENAI_API_KEY=your_key_here
```

4. Run the app:

```bash
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## How To Use

Type in your dream, then press "generate image". If you are a figure in the dream, describe yourself; otherwise the image will assign a body. Image generation can take a bit of time.

## Tests

No automated tests are included in this repo yet. If you add tests later (for example with `pytest`), document the command here.

## Project Report

It was trickier to implement Jungian ideas than I thought it would be — image generation is fairly different from text generation in that you can't just give it a generalized prompt and expect it to do what you want (since it's not following token likelihood in the same way). I researched some Jungian dream analysis, though a lot of it online felt like vague slop?, and tried to incorporate specific archetypes into the image generation prompt. These additional descriptors are added to the user's dream submission in order to give it a more reflective sense. The additional Jungian elements added to the prompt are likely much longer than the initial dream itself, but are all for setting style and mood, though they also add certain elements and objects (like shadows and clocks).

### Reflections

I actually had the time to do more than just the bare minimum for this assignment and I'm grateful for that — I could tweak repeatedly to actually get Jungian elements to show up. I've struggled with image generation prompting before (and frankly still do, but honestly I believe that to be for the best, for the most part) and it takes quite a lot of description to get anything close to what I'm aiming for. Possible improvements would be a better look to the website, and a textural analysis as well, rather than just an image prompt. Maybe trying out a different image model?
