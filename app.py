from flask import Flask, render_template, request, jsonify, send_from_directory
from audio_story_generator import AudioStoryGenerator
import os

# Initialize Flask app
app = Flask(__name__, static_folder='static')

# Define the static directory for generated files
OUTPUT_DIR = os.path.join(app.static_folder)
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main route for rendering the form and processing the topic to generate audio.
    Handles both GET and POST requests.
    """
    if request.method == 'POST':
        topic = request.form.get('topic', '').strip()
        if not topic:
            return jsonify({"status": "error", "message": "Topic is required."}), 400

        # Initialize the audio generator
        generator = AudioStoryGenerator()

        try:
            # Generate the audio story
            output_file_name = 'story_audio.wav'
            output_file_path = os.path.join(OUTPUT_DIR, output_file_name)

            # Use the generator to create the file (example call to a method in the generator)
            generator.generate(topic)

            # Return the relative path to the static file
            file_url = f"/static/{output_file_name}"
            print(f"Generated file URL: {file_url}")
            return jsonify({"status": "success", "file": file_url})
        except Exception as e:
            # Log and return the error message
            print(f"Error generating audio: {e}")
            return jsonify({"status": "error", "message": str(e)}), 500

    # Render the main page for GET requests
    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static_file(filename):
    """
    Route to serve static files from the 'static' directory.
    """
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)
