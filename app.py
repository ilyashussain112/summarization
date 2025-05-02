from flask import Flask, request, render_template
from src.api import get_transcript, preprocessing, generate_audio  # Add generate_audio function

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Debugging print
        print("Form data:", request.form)

        url = request.form.get("url")  # Use get() to avoid KeyError

        if not url:
            return render_template("index.html", summary="No URL provided!")

        video_id = preprocessing(url)
        print("Extracted Video ID:", video_id)  # Debug print

        if not video_id:
            return render_template("index.html", summary="Invalid YouTube URL provided.")

        text = get_transcript(video_id)
        
        # Generate and save audio files
        generate_audio(text, "output_audio_0.wav")
        generate_audio(text, "output_audio_1.wav")  # Assuming two different audio files

        return render_template("index.html", summary=text)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
