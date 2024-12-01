
# **NightSchool AI**  

NightSchool AI is a pioneering application designed to transform sleep into a productive learning experience. By generating calming, educational audio stories tailored to user-specified topics, it enhances memory retention and helps learners grasp challenging concepts during sleep. Built with Flask, OpenAI's GPT models, and a text-to-speech process, NightSchool AI delivers a seamless and user-friendly interface for students and lifelong learners alike.  

---

## **Features**  
- **Topic-Based Story Generation**: Users input a topic, and OpenAI generates a personalized educational story.  
- **Text-to-Speech Conversion**: Stories are converted into soothing audio directly using OpenAI.  
- **Simple, Interactive UI**: Tailored for ease of use, powered by TailwindCSS.  
- **Audio Playback**: Direct playback of generated audio via an in-app player.  

---

## **Deployment**  

NightSchool AI has been deployed using PythonAnywhere with the **basic package ($5/month)**. It is live at:  
[**NightSchool AI Application**](https://saikrupa.pythonanywhere.com/)  

### **Steps for Deployment on PythonAnywhere**:  

1. **Create a PythonAnywhere Account**:  
   Sign up at [pythonanywhere.com](https://www.pythonanywhere.com/) and choose the **Basic Plan ($5/month)** for Flask app hosting.  

2. **Set Up Your Web App**:  
   - Go to the **Web** tab on PythonAnywhere.  
   - Create a new web app by choosing the **Flask Framework** and your preferred Python version.  

3. **Upload Your Project Files**:  
   - Use PythonAnywhere's file manager or SFTP to upload your Flask app files, including `app.py`, `templates`, and `static` folders.  

4. **Install Dependencies**:  
   - Open the PythonAnywhere **Bash Console**.  
   - Install required dependencies using:  
     ```bash
     pip install -r requirements.txt
     ```  

5. **Configure Environment Variables**:  
   - Add your OpenAI API key in the `.env` file or directly in the PythonAnywhere Environment section.  

6. **Run the Web App**:  
   - Restart the web app in the **Web** tab.  
   - Test the live app at your PythonAnywhere domain.  

---

## **Screenshots**  

### **Homepage**  
![Homepage](image.png)  

### **Generated Story with Audio Playback**  
![Generated Story](image.png)  

---

## **How It Works**  

1. **User Input**:  
   Users input the topic they wish to learn about in the provided text area.  

2. **Story Generation**:  
   The app sends the topic to OpenAI's GPT model, which crafts a calming, educational story based on the input.  

3. **Text-to-Speech Conversion**:  
   - The story is processed by OpenAI’s text-to-speech API to generate audio in `.wav` format.  

4. **Audio Playback**:  
   The generated audio file is saved in the `static` directory and played back to the user via an integrated audio player.  

---

## **Setup Instructions**  

### **Prerequisites**  
- Python 3.8+  
- Flask  
- OpenAI API Key  
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

## **Future Enhancements**  
- **PlayHT Integration**: Provide an option for users to select voices and styles for story playback.  
- **Flashcard System**: Save generated audio as flashcards for spaced repetition.  
- **Dynamic Story Modes**: Add options for storytelling styles (e.g., narrative, quiz-based).  
- **User Accounts**: Enable login functionality for saving topics and audio files.  

---

## **Limitations and Considerations**  
- **API Limits**: Ensure your OpenAI API usage is within the allocated limits.  
- **Privacy**: Protect user input and data by implementing robust security measures.  
- **Accuracy**: AI-generated content should be reviewed for accuracy, especially for academic purposes.  

---

## **Support**  
If you encounter any issues or have suggestions, feel free to reach out via [GitHub Issues](https://github.com/your-repo/NightSchool-AI/issues).  

--- 

**Author**: [Sai Krupa Reddy](https://myskr.netlify.app/)  
**License**: MIT License  
