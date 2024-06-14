import speech_recognition as sr
import pyttsx3
import wikipedia

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech_from_mic():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return ""

    return query.lower()

def main():
    speak("Hello, how can I help you today?")
    
    while True:
        query = recognize_speech_from_mic()
        
        if 'exit' in query or 'stop' in query or 'bye' in query:
            speak("Goodbye!")
            break
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple entries for this topic. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("I couldn't find any information on this topic.")
        else:
            speak("Sorry, I can only search Wikipedia for now. Try asking me about a topic to look up.")

if __name__ == "__main__":
    main()
