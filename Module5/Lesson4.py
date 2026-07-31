Detailed Explanation
1. Library Imports

import speech_recognition as sr

import pyttsx3

from googletrans import Translator  # Google Translate API


speech_recognition: Library to convert speech from microphone audio into text.
pyttsx3: Offline Text-to-Speech engine, converts text to spoken words.
googletrans: Python interface to Google Translate API (free and unofficial), used for language translation.

2. Text-to-Speech (speak)

def speak(text, language="en"):

    engine = pyttsx3.init()

    engine.setProperty('rate', 150)  # Speech speed

    voices = engine.getProperty('voices')

   

    if language == "en":

        engine.setProperty('voice', voices[0].id)  # Default English voice

    else:

        engine.setProperty('voice', voices[1].id)  # Fallback voice

   

    engine.say(text)

    engine.runAndWait()


Initializes the TTS engine.
Sets speech rate to 150 words per minute.
Chooses voice depending on language parameter (default English voice or fallback).
Speaks the text aloud.

3. Speech-to-Text (speech_to_text)

def speech_to_text():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("🎤 Please speak now in English...")

        audio = recognizer.listen(source)


    try:

        print("🔍 Recognizing speech...")

        text = recognizer.recognize_google(audio, language="en-US")  # English recognition

        print(f"✅ You said: {text}")

        return text

    except sr.UnknownValueError:

        print("❌ Could not understand the audio.")

    except sr.RequestError as e:

        print(f"❌ API Error: {e}")

    return ""


Uses the microphone to listen to user speech.
Calls Google’s free speech-to-text API to recognize English speech.
Prints recognized text or error messages if speech is unclear or API fails.

4. Translate Text (translate_text)

def translate_text(text, target_language="es"):

    translator = Translator()

    translation = translator.translate(text, dest=target_language)

    print(f"🌍 Translated text: {translation.text}")

    return translation.text


Uses googletrans to translate recognized English text to the specified target language.
Default target is Spanish ("es"), but your program changes it dynamically.

5. Language Selection (display_language_options)

def display_language_options():

    print("🌍 Available translation languages: ")

    print("1. Hindi (hi)")

    print("2. Tamil (ta)")

    print("3. Telugu (te)")

    print("4. Bengali (bn)")

    print("5. Marathi (mr)")

    print("6. Gujarati (gu)")

    print("7. Malayalam (ml)")

    print("8. Punjabi (pa)")


    choice = input("Please select the target language number (1-8): ")

    language_dict = {

        "1": "hi", "2": "ta", "3": "te", "4": "bn",

        "5": "mr", "6": "gu", "7": "ml", "8": "pa"

    }

    return language_dict.get(choice, "es")  # Default Spanish if invalid


Shows a menu of Indian languages.
Takes user choice and maps it to Google Translate language codes.
Defaults to Spanish if the choice is invalid.

6. Main Flow

def main():

    target_language = display_language_options()  # Choose language

    original_text = speech_to_text()              # Convert speech to text


    if original_text:

        translated_text = translate_text(original_text, target_language=target_language)  # Translate

        speak(translated_text, language="en")   # Speak translated text aloud (still English voice)

        print("✅ Translation spoken out!")


Activity Name : Speech-to-Text Translator with Voice Output

Activity Description :  
This program listens to your spoken English, converts it to text, translates it into a chosen language, and then speaks out the translated text using text-to-speech.

Activity Code :

import speech_recognition as sr

import pyttsx3

from googletrans import Translator  # Google Translate API


# Initialize text-to-speech engine

def speak(text, language="en"):

    engine = pyttsx3.init()

    engine.setProperty('rate', 150)  # Speed of speech

    voices = engine.getProperty('voices')

   

    # Set voice for English or other language if supported by pyttsx3

    if language == "en":

        engine.setProperty('voice', voices[0].id)  # Default English voice

    else:

        engine.setProperty('voice', voices[1].id)  # Fallback to another voice if available

   

    engine.say(text)

    engine.runAndWait()


# Speech-to-Text: Recognize spoken language (English)

def speech_to_text():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("🎤 Please speak now in English...")

        audio = recognizer.listen(source)


    try:

        print("🔍 Recognizing speech...")

        text = recognizer.recognize_google(audio, language="en-US")  # Use English for speech recognition

        print(f"✅ You said: {text}")

        return text

    except sr.UnknownValueError:

        print("❌ Could not understand the audio.")

    except sr.RequestError as e:

        print(f"❌ API Error: {e}")

    return ""


# Translate text using Google Translate API

def translate_text(text, target_language="es"):  # Default target language is Spanish (es)

    translator = Translator()

    translation = translator.translate(text, dest=target_language)

    print(f"🌍 Translated text: {translation.text}")

    return translation.text


# Display language options to the user

def display_language_options():

    print("🌍 Available translation languages: ")

    print("1. Hindi (hi)")

    print("2. Tamil (ta)")

    print("3. Telugu (te)")

    print("4. Bengali (bn)")

    print("5. Marathi (mr)")

    print("6. Gujarati (gu)")

    print("7. Malayalam (ml)")

    print("8. Punjabi (pa)")


    # User selects language

    choice = input("Please select the target language number (1-8): ")

    language_dict = {

        "1": "hi",

        "2": "ta",

        "3": "te",

        "4": "bn",

        "5": "mr",

        "6": "gu",

        "7": "ml",

        "8": "pa"

    }

   

    return language_dict.get(choice, "es")  # Default to Spanish if invalid input


# Main function to combine all steps

def main():

    # Step 1: Display language options and get user's choice

    target_language = display_language_options()

   

    # Step 2: Speech-to-Text (recognizing English speech)

    original_text = speech_to_text()

   

    if original_text:

        # Step 3: Translate to selected target language

        translated_text = translate_text(original_text, target_language=target_language)

       

        # Step 4: Text-to-Speech (Translate output and speak it)

        speak(translated_text, language="en")  # Speak the translation in English

        print("✅ Translation spoken out!")


if __name__ == "__main__":

    main()

