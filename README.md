
# **NightSchool AI**  

NightSchool AI is a pioneering application designed to transform sleep into a productive learning experience. By generating calming, educational audio stories tailored to user-specified topics, it enhances memory retention and helps learners grasp challenging concepts during sleep. Built with Flask, OpenAI's GPT models, and a text-to-speech process, NightSchool AI delivers a seamless and user-friendly interface for students and lifelong learners alike.  

---

## **Features**  
- **Topic-Based Story Generation**: Users input a topic, and OpenAI generates a personalized educational story.  
- **Text-to-Speech Conversion**: Stories are converted into soothing audio directly using OpenAI. Alternatively, PlayHT can also be utilized for enhanced text-to-speech capabilities.  
- **Simple, Interactive UI**: Tailored for ease of use, powered by TailwindCSS.  
- **Audio Playback**: Direct playback of generated audio via an in-app player.  

---

## **How It Works**  

1. **User Input**:  
   Users input the topic they wish to learn about in the provided text area.  

2. **Story Generation**:  
   The app sends the topic to OpenAI's GPT model, which crafts a calming, educational story based on the input.  

3. **Text-to-Speech Conversion**:  
   - **Option 1**: Using OpenAI's integrated text-to-speech feature, the story is converted into an audio file in `.wav` format.  
   - **Option 2 (Future Enhancement)**: Use PlayHT API to convert text into audio for additional voice options and customization.  

4. **Audio Playback**:  
   The generated audio file is saved in the `static` directory and played back to the user via an integrated audio player.  

---

## **Setup Instructions**  

### **Prerequisites**  
- Python 3.8+  
- Flask  
- OpenAI API Key  
- (Optional) PlayHT API Key  
- TailwindCSS (optional for customization)  

### **Installation**  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-repo/NightSchool-AI.git
   cd NightSchool-AI
   ```  

2. Install required dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

3. Create a `.env` file in the project root and add your API keys:  
   ```plaintext
   OPENAI_API_KEY=<your_openai_api_key>
   PLAYHT_API_KEY=<your_playht_api_key>  # Optional if PlayHT will be used
   ```  

4. Ensure the `static` folder exists in the project directory to store generated audio files.  
   ```bash
   mkdir static
   ```  

5. Run the Flask app:  
   ```bash
   python app.py
   ```  

6. Open your browser and navigate to `http://127.0.0.1:5000/`.  

---

## **Usage Instructions**  

1. Enter the topic you want to learn about in the text area on the homepage (e.g., "The Solar System").  
2. Click the **"Generate Story"** button.  
3. Wait while the app generates and processes your story.  
4. Once completed, the audio player will appear with your generated story ready to play.  

---

## **File Structure**  
- `app.py`: Main Flask application.  
- `audio_story_generator.py`: Contains the `AudioStoryGenerator` class for generating stories and audio.  
- `templates/index.html`: HTML template for the user interface.  
- `static/`: Directory for storing generated audio files.  
- `.env`: File for storing API keys securely.  

---

## **How It Really Works**  

### **Story Generation**  
1. The `fetch_story_from_openai()` function sends the user's topic to the OpenAI API using a carefully crafted prompt.  
2. The AI responds with an educational, engaging story tailored to the topic.  

### **Text-to-Speech Conversion**  
1. Using OpenAI:  
   - The story is processed by OpenAI’s text-to-speech API to generate audio in `.wav` format.  

2. **(Optional Enhancement)** Using PlayHT:  
   - The story is sent to the PlayHT API for advanced text-to-speech conversion, allowing users to select voices and styles.  

3. The generated audio is saved in the `static` directory for easy access.  

### **User Interface**  
1. The Flask app renders the `index.html` template, which provides a user-friendly interface styled with TailwindCSS.  
2. JavaScript handles form submission, sending the user's input to the Flask backend and updating the page with the generated audio.  

---

## **Future Enhancements**  
- **PlayHT Integration**: Provide an option for users to select voices and styles for story playback.  
- **Flashcard System**: Save generated audio as flashcards for spaced repetition.  
- **Dynamic Story Modes**: Add options for storytelling styles (e.g., narrative, quiz-based).  
- **User Accounts**: Enable login functionality for saving topics and audio files.  

---

## **Limitations and Considerations**  
- **API Limits**: Ensure your OpenAI and PlayHT API usage is within the allocated limits.  
- **Privacy**: Protect user input and data by implementing robust security measures.  
- **Accuracy**: AI-generated content should be reviewed for accuracy, especially for academic purposes.  

---

## **Support**  
If you encounter any issues or have suggestions, feel free to reach out via [GitHub Issues](https://github.com/your-repo/NightSchool-AI/issues).  

--- 

**Author**: [Sai Krupa Reddy](https://myskr.netlify.app/)  
**License**: MIT License  
