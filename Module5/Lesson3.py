1. Library Imports:

import random


The random library is imported to randomly select one of the fun sample phrases that the AI will speak, adding a playful touch to the interaction.
2. Handling Text-to-Speech (TTS) Availability:

try:

    import pyttsx3

    TTS_AVAILABLE = True

except ImportError:

    TTS_AVAILABLE = False

    print("⚠️  Run: pip install pyttsx3")


The script first tries to import the pyttsx3 library, which provides the text-to-speech functionality. If the import is successful, a flag TTS_AVAILABLE is set to True, indicating that TTS is available.
If the pyttsx3 library is not installed or there is an issue with the import, the TTS_AVAILABLE flag is set to False and the script prints a warning message to inform the user to install the necessary package by running pip install pyttsx3.
3. TTS Setup Function:

def setup_tts():

    """Initialize text-to-speech"""

    if not TTS_AVAILABLE:

        return None

    try:

        engine = pyttsx3.init()

        engine.setProperty("rate", 150)

        engine.setProperty("volume", 0.9)

        return engine

    except:

        return None


Purpose: Initializes the text-to-speech engine.
First, it checks if TTS_AVAILABLE is True. If not, the function returns None, indicating that TTS is unavailable.
If TTS is available, it initializes the TTS engine using pyttsx3.init(), which prepares the engine to speak.
engine.setProperty("rate", 150) sets the speech rate (speed of speech) to 150 words per minute.
engine.setProperty("volume", 0.9) sets the volume of the speech to 90% of the maximum.
If the engine cannot be initialized (due to some issue), it returns None.
4. Speech Function:

def speak(engine, text):

    """Speak text or show fallback"""

    if engine:

        try:

            engine.say(text)

            engine.runAndWait()

        except:

            print(f"🔇 [AUDIO]: {text}")

    else:

        print(f"🔇 [AUDIO]: {text}")


Purpose: This function takes the initialized TTS engine and a string of text, and converts the text into speech.
It first checks if the engine is available (i.e., TTS is enabled). If available, it calls engine.say(text) to queue the text for speech.
engine.runAndWait() is called to actually perform the speech synthesis and wait for the speech to finish.
If an exception occurs while trying to speak (e.g., TTS issues or environment restrictions), it prints a fallback message: 🔇 [AUDIO]: {text} to indicate the issue.
If TTS is not available (engine is None), it directly prints the text to the console instead of speaking it.
5. Fun Phrases:

def get_samples():

    """Fun phrases to try"""

    return [

        "Hello! I am your computer!",

        "Python is awesome!",

        "This is AI speaking!",

        "Welcome to the future!"

    ]


Purpose: This function returns a list of predefined fun phrases that the AI can speak randomly.
It adds a fun element to the interaction, allowing the user to hear some interesting or playful sentences from the AI.
6. Main Program Loop:

def main():

    print("🤖 AI VOICE LAB")

    print("===============")

   

    engine = setup_tts()

   

    if engine:

        print("✅ Voice ready! Try typing something...")

    else:

        print("⚠️  No audio, but you can still learn!")

   

    speak(engine, "Hello! Type something for me to say!")

   

    while True:

        text = input("\n🎤 You: ").strip()

       

        if text.lower() == 'exit':

            speak(engine, "Goodbye!")

            break

        elif text.lower() == 'sample':

            phrase = random.choice(get_samples())

            print(f"🎲 {phrase}")

            speak(engine, phrase)

        elif text:

            speak(engine, text)

        else:

            print("💡 Type 'sample' for ideas or 'exit' to quit")


Purpose: This is the core function where the program interacts with the user.
Initialize TTS Engine:
The script first prints the title of the program: "AI VOICE LAB" and initializes the TTS engine using setup_tts().
If the TTS engine is initialized successfully, it prints "✅ Voice ready! Try typing something..." otherwise, it warns "⚠️ No audio, but you can still learn!"
Speak Initial Message:
If TTS is available, it uses the speak() function to say a welcome message: "Hello! Type something for me to say!".
Main Interaction Loop:
The while True loop keeps the program running, awaiting user input.
If the user types 'exit', the program will say "Goodbye!" and exit the loop.
If the user types 'sample', a random phrase from get_samples() is selected and spoken by the AI.
If the user types any other text, the program will speak the entered text using the TTS engine.
If the user enters nothing (an empty string), the program suggests typing 'sample' or 'exit'.
7. Program Exit:
When the user types 'exit', the program says "Goodbye!" and exits the loop, terminating the program.
Summary of the Key Features:
Text-to-Speech Functionality: Uses the pyttsx3 library to convert text into speech.
Interactive Voice Lab: The user interacts with the program by typing input, and the program speaks out the responses.
Random Fun Phrases: The user can ask the program to say random fun phrases to make the interaction more enjoyable.
Exit Command: The user can type 'exit' to terminate the program.
Conclusion:
This script demonstrates how to set up an interactive TTS-based application using Python and the pyttsx3 library. It handles voice output and includes basic error handling for missing dependencies. The program is intended to be fun and educational, offering the user an opportunity to interact with an AI in a playful manner.




Conclusion:
This activity provides students with a solid foundation for integrating TTS into Python applications. By learning how to handle user input, create dynamic interactions, and use voice feedback, students gain hands-on experience in building interactive AI systems. These skills are foundational for developing AI systems that can communicate with users audibly, a feature increasingly prevalent in personal assistants, educational tools, and interactive applications.




Activity title: AI Voice Lab: Interactive Text-to-Speech

Description:
This interactive Python program uses the pyttsx3 library to provide text-to-speech functionality, where users can type in questions or prompts and hear the AI's response. It includes features like random sample phrases and a simple exit mechanism, offering an engaging experience for learning and fun.



Code


import random


# Try importing TTS library

try:

    import pyttsx3

    TTS_AVAILABLE = True

except ImportError:

    TTS_AVAILABLE = False

    print("⚠️  Run: pip install pyttsx3")


def setup_tts():

    """Initialize text-to-speech"""

    if not TTS_AVAILABLE:

        return None

    try:

        engine = pyttsx3.init()

        engine.setProperty("rate", 150)

        engine.setProperty("volume", 0.9)

        return engine

    except:

        return None


def speak(engine, text):

    """Speak text or show fallback"""

    if engine:

        try:

            engine.say(text)

            engine.runAndWait()

        except:

            print(f"🔇 [AUDIO]: {text}")

    else:

        print(f"🔇 [AUDIO]: {text}")


def get_samples():

    """Fun phrases to try"""

    return [

        "Hello! I am your computer!",

        "Python is awesome!",

        "This is AI speaking!",

        "Welcome to the future!"

    ]


def main():

    print("🤖 AI VOICE LAB")

    print("===============")

   

    engine = setup_tts()

   

    if engine:

        print("✅ Voice ready! Try typing something...")

    else:

        print("⚠️  No audio, but you can still learn!")

   

    speak(engine, "Hello! Type something for me to say!")

   

    while True:

        text = input("\n🎤 You: ").strip()

       

        if text.lower() == 'exit':

            speak(engine, "Goodbye!")

            break

        elif text.lower() == 'sample':

            phrase = random.choice(get_samples())

            print(f"🎲 {phrase}")

            speak(engine, phrase)

        elif text:

            speak(engine, text)

        else:

            print("💡 Type 'sample' for ideas or 'exit' to quit")


if __name__ == "__main__":

    main()





Learning Outcomes:
Mastering Text-to-Speech (TTS): Students will learn how to convert text to speech using Python and pyttsx3.
Handling User Input: Learn how to handle user input in command-line applications.
Incorporating Randomness: Use randomness to make AI responses more dynamic and engaging.
Error Handling: Implement error handling for missing libraries and dependencies.
Voice Feedback: Develop an AI that can interact with users through audible feedback.
Building Interactive Voice Applications: Build an AI that continuously interacts with the user, simulating a conversation.
Practical Application: Understand the importance of TTS in accessibility and AI applications, laying the groundwork for more complex voice-based projects


Teacher’s Agenda: Interactive AI Voice Application (Text-to-Speech) for 1:1 and 1:n Class

1:1 Class (45 Minutes)

1. Introduction to the Lesson (5 minutes)

Objective: Introduce the concept of Text-to-Speech (TTS) technology and its applications.
Activity: Briefly explain TTS, its real-world applications (e.g., voice assistants like Siri or Alexa), and its importance in AI interactions.
Discussion: Ask the student about their previous experience with AI or voice-based applications.

2. Library Setup and Importing pyttsx3 (5 minutes)

Objective: Guide the student to install and import the pyttsx3 library.
Activity: Show how to run pip install pyttsx3 and verify that the installation works.
Troubleshooting: If any errors occur, briefly explain how to address them (e.g., missing libraries).

3. Initializing the TTS Engine (8 minutes)

Objective: Teach the student how to initialize the pyttsx3 engine and set basic properties (rate and volume).
Activity: Walk through the setup_tts() function, explaining how to modify the speech rate and volume.
Hands-on: Let the student test the function by adjusting the rate and volume, allowing them to experiment with different settings.

4. Speech Output with speak() Function (7 minutes)

Objective: Demonstrate how the student can convert text into speech using the speak() function.
Activity: Show how to pass different text inputs and convert them to speech.
Hands-on: Allow the student to input different phrases and observe the speech output.

5. Adding Randomness to Responses (5 minutes)

Objective: Show the student how to make the AI respond with random, fun phrases.
Activity: Demonstrate the random.choice() function to select random phrases.
Hands-on: Let the student modify the list of sample phrases and test different responses.

6. Continuous Interaction with Looping (7 minutes)

Objective: Introduce the concept of looping for continuous interaction with the AI.
Activity: Walk through the while loop that keeps the program running, allowing the user to keep interacting with the AI.
Hands-on: Guide the student to test the loop by entering different inputs and observing the AI’s response.

7. Wrapping Up the Lesson (3 minutes)

Objective: Summarize the key points learned during the class.
Discussion: Ask the student to share their thoughts on how they can use this TTS functionality in their own projects or applications.

8. Assignment and Next Steps (3 minutes)

Objective: Assign a task to further explore TTS or related topics.
Activity: Ask the student to modify the program to include additional phrases, or add an interactive feature (e.g., requesting specific jokes or facts).
Next Class Prep: Let the student know that the next lesson will build upon these interactive concepts.

Total Time: 45 minutes


1:n Class (60 Minutes)

1. Introduction to the Lesson (8 minutes)

Objective: Introduce TTS technology and discuss its applications.
Activity: Briefly explain TTS and its relevance in AI systems like voice assistants. Use a short video or example to illustrate real-world use.
Discussion: Have students briefly share their experiences with voice-based applications like Siri or Alexa.

2. Library Setup and Importing pyttsx3 (7 minutes)

Objective: Walk the class through installing the pyttsx3 library and importing it.
Activity: Show how to install pyttsx3 using pip install pyttsx3. Ensure that everyone has it installed.
Troubleshooting: Address common installation issues (e.g., missing packages).

3. Initializing the TTS Engine (10 minutes)

Objective: Teach how to initialize the pyttsx3 engine and adjust its properties.
Activity: Explain how to set the rate and volume of speech. Demonstrate the setup_tts() function with the class.
Hands-on: Have students run the function on their own systems, testing different values for speech rate and volume.

4. Implementing Speech Output with speak() Function (10 minutes)

Objective: Show how to use the speak() function to convert text to speech.
Activity: Demonstrate how to input text and use speak() to hear it aloud.
Hands-on: Ask students to input text and test how it’s spoken by the AI.

5. Adding Random Phrases to Enhance Responses (8 minutes)

Objective: Explain how to incorporate randomness into responses using random.choice().
Activity: Walk the class through adding fun phrases that the AI can randomly say.
Hands-on: Ask students to add their own phrases to the list and test the randomness.

6. Looping for Continuous Interaction (10 minutes)

Objective: Teach how to create a loop for continuous interaction with the AI.
Activity: Demonstrate the while loop to allow for ongoing input from the user.
Hands-on: Guide students to test the loop and explore how to make the AI respond to different commands (e.g., “exit” to end).

7. Wrapping Up and Summary (5 minutes)

Objective: Recap the key concepts and steps covered during the lesson.
Discussion: Open the floor for any questions. Ask students how they can use this functionality in their future projects.

8. Assignment and Next Steps (5 minutes)

Objective: Provide students with an assignment to build upon the concepts learned in class.
Activity: Assign students to enhance their program with additional features, such as handling more complex user inputs or adding functionality like asking for jokes or weather updates.
Preview of Next Lesson: Briefly discuss how the next lesson will build on voice-enabled AI systems.

Total Time: 60 minutes


Summary:
In 1:1 classes, the focus is on a personalized pace, with hands-on activities and plenty of time for troubleshooting. 1:n classes involve more collaborative discussions, hands-on activities with some group interaction, and a larger focus on addressing common issues as a class. In both sessions, the teacher should ensure that students are actively engaged, with a solid grasp of each concept through testing and experimentation.



Lesson Quiz




Q1: What is the main purpose of the pyttsx3 library in this code?
✅ Correct Answer:
 a) To convert text into speech
 Explanation:
 The pyttsx3 library is used to convert text input into speech, making it the core component for text-to-speech (TTS) functionality in this application.

a) To convert text into speech
b) To handle user input from the command line
c) To generate random phrases
d) To display text-based responses in the terminal

Q2: How does the program handle the case when the pyttsx3 library is not installed?
✅ Correct Answer:
 a) It sets the TTS_AVAILABLE flag to False and suggests installing the library using pip install pyttsx3
 Explanation:
 The program uses a try-except block to check if the pyttsx3 library is available. If not, it sets the TTS_AVAILABLE flag to False and prompts the user to install the library.

a) It sets the TTS_AVAILABLE flag to False and suggests installing the library using pip install pyttsx3
b) It automatically installs the library without notifying the user
c) It exits the program immediately
d) It generates an error and stops the program

Q3: What does the setup_tts function do?
✅ Correct Answer:
 a) It initializes the TTS engine and sets properties like speech rate and volume
 Explanation:
 The setup_tts function initializes the pyttsx3 TTS engine and sets properties like speech rate and volume to customize the voice output.

a) It initializes the TTS engine and sets properties like speech rate and volume
b) It checks if the TTS library is installed
c) It handles user input for TTS output
d) It generates random phrases for the program to speak

Q4: What happens when the user types 'sample' in the interactive loop?
✅ Correct Answer:
 a) The program randomly selects a phrase from the get_samples() function and speaks it aloud
 Explanation:
 When the user types 'sample', the program randomly selects one of the predefined fun phrases and speaks it using the TTS engine.

a) The program randomly selects a phrase from the get_samples() function and speaks it aloud
b) The program exits immediately
c) The program repeats the user's last input
d) The program asks the user to type another command

Q5: What is the purpose of the get_samples function in the code?
✅ Correct Answer:
 a) To provide a list of fun phrases that the AI can speak randomly
 Explanation:
 The get_samples function returns a list of predefined fun phrases that the AI can say, making the interaction more engaging and playful.

a) To provide a list of fun phrases that the AI can speak randomly
b) To handle user input in the terminal
c) To generate the speech rate and volume settings
d) To initialize the TTS engine

Q6: In the speak function, what happens if the TTS engine is not available?
✅ Correct Answer:
 a) It prints the text to the console instead of speaking it aloud
 Explanation:
 If the TTS engine is not available (i.e., the engine is None), the speak function prints the text to the console instead of generating speech.

a) It prints the text to the console instead of speaking it aloud
b) It silently ignores the text and does nothing
c) It generates a default response
d) It crashes the program with an error

Q7: How does the program ensure continuous interaction with the user in the main loop?
✅ Correct Answer:
 a) It uses a while True loop that keeps the program running until the user types 'exit'
 Explanation:
 The while True loop ensures continuous interaction by repeatedly asking for user input and responding until the user types 'exit'.

a) It uses a while True loop that keeps the program running until the user types 'exit'
b) It uses a for loop that limits interactions to 5 rounds
c) It only responds to a predefined set of commands
d) It automatically terminates after a certain period of time

Q8: What does the rate property in the TTS engine control?
✅ Correct Answer:
 a) It controls the speed at which the text is spoken
 Explanation:
 The rate property adjusts the speech rate (speed of speech) of the TTS engine, making the AI speak faster or slower based on the specified value.

a) It controls the speed at which the text is spoken
b) It controls the volume of the speech
c) It controls the pitch of the speech
d) It controls the language used by the AI

Q9: What is the behavior of the program when the user types 'exit'?
✅ Correct Answer:
 a) The program says "Goodbye!" and exits the loop, terminating the program
 Explanation:
 When the user types 'exit', the program says "Goodbye!" and breaks out of the loop, ending the interaction.

a) The program says "Goodbye!" and exits the loop, terminating the program
b) The program asks the user if they are sure about exiting
c) The program restarts the entire process from the beginning
d) The program waits for the user to type another command

Q10: What is the role of the random.choice() function in the code?
✅ Correct Answer:
 a) It randomly selects a phrase from the predefined list of fun phrases
 Explanation:
 The random.choice() function selects a random phrase from the list returned by the get_samples() function, making the interaction more dynamic.

a) It randomly selects a phrase from the predefined list of fun phrases
b) It generates a random number to adjust the TTS engine's properties
c) It shuffles the order of commands in the program
d) It exits the program when the user types 'sample'


After-Class Assignment for Building an Interactive AI Voice Application: Text-to-Speech (TTS) with Python

Title: Enhancing Your AI Voice Application

Description:
 In this assignment, you will reinforce your learning from the lesson by extending the functionality of your AI Voice Application. You'll enhance your program by adding more interactivity and customizing the voice responses. This is an opportunity to practice handling user input, adding more dynamic features, and improving the overall functionality of your TTS-based application.


Goal:
Reinforce the concepts of Text-to-Speech (TTS) and user input handling.
Implement randomness in AI responses.
Experiment with different speech rates and volumes.
Create a more interactive AI application that can respond to different commands.

Getting Started:
Ensure that you have successfully completed the lesson on creating a Text-to-Speech interactive application with the pyttsx3 library. You can refer to the code provided in class to get started with the basic structure.


Instructions:
Create a List of Custom Phrases:
 Extend the list of random phrases. Add at least five more fun or interesting phrases that the AI can say, such as quotes, jokes, or famous sayings.
Add Speech Rate and Volume Control:
 Implement user-controlled speech rate and volume. The user should be able to enter a command like "speed up" or "slow down" to modify the speech rate, or "increase volume" or "decrease volume" to adjust the volume.
Create a Custom Command:
 Add a custom command that when typed (e.g., "tell a joke"), the AI will speak a random joke from a predefined list.
Error Handling:
 Implement an error handling feature for invalid commands. If the user types something the AI doesn't recognize, the AI should respond with a friendly message (e.g., "I didn't quite catch that. Try again!").
Looping and Continuous Interaction:
 Ensure the program keeps interacting with the user until the "exit" command is entered. Make sure the program provides feedback when commands are successfully executed or when errors occur.

Hint (Solution with Complete Working Code):
python

Copy

import random

import pyttsx3


# Initialize pyttsx3 TTS engine

engine = pyttsx3.init()

engine.setProperty("rate", 150)

engine.setProperty("volume", 0.9)


def speak(text):

    """Speak the text provided to the TTS engine."""

    engine.say(text)

    engine.runAndWait()


def get_samples():

    """Return a list of custom phrases and jokes."""

    return [

        "Hello! I am your computer!",

        "Python is awesome!",

        "This is AI speaking!",

        "Welcome to the future!",

        "Why don't skeletons fight each other? They don't have the guts!"

    ]


def main():

    print("🤖 AI VOICE LAB")

    speak("Hello! Type something for me to say!")

   

    while True:

        text = input("\n🎤 You: ").strip().lower()

       

        # Exit Command

        if text == 'exit':

            speak("Goodbye!")

            break

       

        # Random Sample Command

        elif text == 'sample':

            phrase = random.choice(get_samples())

            print(f"🎲 {phrase}")

            speak(phrase)

       

        # Custom Commands for Speed and Volume

        elif text == 'speed up':

            current_rate = engine.getProperty('rate') + 50

            engine.setProperty('rate', current_rate)

            speak(f"Speed increased to {current_rate}")

       

        elif text == 'slow down':

            current_rate = engine.getProperty('rate') - 50

            engine.setProperty('rate', current_rate)

            speak(f"Speed decreased to {current_rate}")

       

        elif text == 'increase volume':

            current_volume = engine.getProperty('volume') + 0.1

            if current_volume > 1: current_volume = 1

            engine.setProperty('volume', current_volume)

            speak(f"Volume increased to {current_volume}")

       

        elif text == 'decrease volume':

            current_volume = engine.getProperty('volume') - 0.1

            if current_volume < 0: current_volume = 0

            engine.setProperty('volume', current_volume)

            speak(f"Volume decreased to {current_volume}")

       

        # Custom Command for Jokes

        elif text == 'tell a joke':

            jokes = [

                "Why don't skeletons fight each other? They don't have the guts!",

                "What do you get when you cross a snowman and a vampire? Frostbite!",

                "Why don’t scientists trust atoms? Because they make up everything!"

            ]

            joke = random.choice(jokes)

            print(f"😂 {joke}")

            speak(joke)

       

        # Unrecognized Command

        else:

            print("💡 Type 'sample' for ideas or 'exit' to quit.")

            speak("I didn't quite catch that. Try again!")


if __name__ == "__main__":

    main()



Additional Hints:
Customizing Speech:
 Use engine.setProperty("rate", value) to modify how fast or slow the speech is. Experiment with values like 120, 150, and 200 for different speeds.
Volume Control:
 The engine.setProperty("volume", value) allows for volume adjustments. Values range from 0.0 (mute) to 1.0 (full volume).
Title
🎙️ Voice Master+: Extend Your Talking AI


Objective
To reinforce core concepts of Text-to-Speech (TTS), user input handling, randomness, and command interpretation by upgrading the original AI Voice Lab into a more interactive and responsive application.


Goal
Students will build on the lesson project by:

Expanding random responses (using lists)
Adding custom commands for jokes and speech controls
Implementing error-handling for unknown inputs
Practicing dynamic interaction using loops

Getting Started
Open the code you built during class (ai_voice_lab.py)
Ensure pyttsx3 is installed:

pip install pyttsx3

Copy the full code below into a new file named voice_master_plus.py
Run the program and interact using voice commands!

Instruction
Add 5 or more fun new phrases to the get_samples() list.
Add speech rate and volume control:
speed up, slow down
increase volume, decrease volume
Add a custom command:
tell a joke → AI speaks a random joke.
Add error handling:
If command not understood, reply with: “I didn’t quite catch that. Try again!”
Keep the loop running until exit is typed.

Hint (Complete Code Solution)

import random

import pyttsx3


# Initialize pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 150)

engine.setProperty("volume", 0.9)


def speak(text):

    """Convert text to speech"""

    engine.say(text)

    engine.runAndWait()


def get_samples():

    return [

        "Hello! I am your computer!",

        "Python is awesome!",

        "This is AI speaking!",

        "Welcome to the future!",

        "Never give up on learning!",

        "AI can be fun and helpful!",

        "Speak your thoughts into code!"

    ]


def main():

    print("🤖 VOICE MASTER+")

    speak("Hello! Type something for me to say!")


    while True:

        user_input = input("\n🎤 You: ").strip().lower()


        if user_input == "exit":

            speak("Goodbye! See you next time.")

            break


        elif user_input == "sample":

            phrase = random.choice(get_samples())

            print(f"🎲 {phrase}")

            speak(phrase)


        elif user_input == "speed up":

            rate = engine.getProperty("rate") + 50

            engine.setProperty("rate", rate)

            speak(f"Speaking faster now at {rate} rate.")


        elif user_input == "slow down":

            rate = engine.getProperty("rate") - 50

            engine.setProperty("rate", rate)

            speak(f"Speaking slower now at {rate} rate.")


        elif user_input == "increase volume":

            vol = engine.getProperty("volume") + 0.1

            vol = min(1.0, vol)

            engine.setProperty("volume", vol)

            speak("Volume increased.")


        elif user_input == "decrease volume":

            vol = engine.getProperty("volume") - 0.1

            vol = max(0.0, vol)

            engine.setProperty("volume", vol)

            speak("Volume decreased.")


        elif user_input == "tell a joke":

            jokes = [

                "Why don't scientists trust atoms? Because they make up everything!",

                "What do you call fake spaghetti? An impasta!",

                "I told my computer I needed a break, and it said: 'No problem, I’ll go to sleep!'"

            ]

            joke = random.choice(jokes)

            print(f"😂 {joke}")

            speak(joke)


        elif user_input:

            speak(user_input)


        else:

            print("💡 Type 'sample', 'tell a joke', or 'exit'")

            speak("I didn’t quite catch that. Try again!")


if __name__ == "__main__":

    main()


