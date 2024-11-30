from openai import OpenAI
import os
from dotenv import load_dotenv
import wave
import numpy as np
import soundfile as sf
from scipy.signal import resample
from pathlib import Path
import base64
from flask import Flask, Response, request, jsonify, stream_with_context
# Load environment variables
load_dotenv()

# Initialize OpenAI API
client = OpenAI()


def fetch_story_from_openai(topic: str) -> str:
    """
    Fetch a story from OpenAI based on the given topic.
    """
    prompt = (
        f"Craft a calming, educational story for nighttime learning that teaches key concepts of '{topic}'. "
        "Ensure the story is engaging, easy to follow, and promotes memory retention."
    )
    
    # Make the API call using the ChatGPT model
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Specify the correct model
        messages=[
            {"role": "system", "content": "You are a creative writer skilled in educational storytelling."},
            {"role": "user", "content": prompt}
        ],
    )

    # Extract the generated story from the response
    return response.choices[0].message.content

from pathlib import Path
import openai

def split_text_into_chunks(text, max_length=4096):
    """
    Splits the input text into smaller chunks to fit the API limit.
    """
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        # Add the word if it doesn't exceed the max length
        if len(" ".join(current_chunk + [word])) <= max_length:
            current_chunk.append(word)
        else:
            # Save the current chunk and start a new one
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]

    # Add the last chunk
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def generate_audio(text: str, output_file: str = "static/story_audio.wav"):
    """
    Generate an audio file from the text using OpenAI's text-to-speech API.
    """
    audio_data = b""
    text_chunks = split_text_into_chunks(text, max_length=4096)

    for chunk in text_chunks:
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=chunk,
            response_format="wav"
        )
        for audio_chunk in response.iter_bytes(1024):
            audio_data += audio_chunk

    with open(output_file, "wb") as audio_file:
        audio_file.write(audio_data)
    
    print(f"Audio file generated: {output_file}")
    return output_file


# Example usage
if __name__ == "__main__":
    text = "Your long input text goes here."
    generate_audio(text)


class AudioStoryGenerator:
    def generate(self, topic: str):
        """
        Main method to generate an audio story.
        """
        # Fetch the story from OpenAI
        story = fetch_story_from_openai(topic)
        
        # Generate audio from the story
        speech_file_path = generate_audio(story)

        
        return "story_audio.wav"
