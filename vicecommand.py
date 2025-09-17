import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pywhatkit
import sys

# ---- voice + TTS setup ----
LANG = "en-IN"  # tweak if you prefer en-US, etc.

engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# ---- speech to text ----
def listen(prompt="Listening..."):
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.dynamic_energy_threshold = True
    with sr.Microphone() as source:
        print(prompt)
        r.adjust_for_ambient_noise(source, duration=0.6)
        audio = r.listen(source, phrase_time_limit=6)
    try:
        return r.recognize_google(audio, language=LANG).lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Network error. Please check your internet connection.")
        return ""

# ---- command handlers ----
def handle_command(cmd: str) -> bool:
    """
    Return True to continue, False to exit.
    """
    if not cmd:
        speak("Sorry, I didn't catch that.")
        return True

    print("You said:", cmd)

    if any(word in cmd for word in ["exit", "quit", "stop"]):
        speak("Okay, bye!")
        return False

    # time
    if "time" in cmd:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}.")
        return True

    # open youtube
    if "open youtube" in cmd:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
        return True

    # google search
    if cmd.startswith("search ") or "search for" in cmd:
        query = cmd.replace("search for", "").replace("search", "").strip()
        if query:
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)
            speak(f"Searching Google for {query}.")
        else:
            speak("What should I search for?")
        return True 
    
    # chatGPT query (placeholder)
    if cmd.startswith("ask chatgpt ") or "ask chatgpt" in cmd:
        query = cmd.replace("ask chatgpt", "").strip()
        if query:
            url = f"htttps://www.chatgpt.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)
            speak(f"Asking ChatGPT about {query}.")
        else:
            speak("What should I ask ChatGPT?")
        return True
    


    # play song/video on YouTube
    if cmd.startswith("play ") or "play on youtube" in cmd:
        query = cmd.replace("play on youtube", "").replace("play", "").strip()
        if query:
            speak(f"Playing {query} on YouTube.")
            pywhatkit.playonyt(query)
        else:
            speak("What should I play?")
        return True

    # wikipedia summary
    if "wikipedia" in cmd or cmd.startswith("who is") or cmd.startswith("what is"):
        topic = cmd.replace("wikipedia", "").replace("who is", "").replace("what is", "").strip()
        if topic:
            try:
                summary = wikipedia.summary(topic, sentences=2, auto_suggest=False, redirect=True)
                speak(summary)
            except Exception:
                speak("I couldn't fetch Wikipedia for that topic.")
        else:
            speak("Please say a topic for Wikipedia.")
        return True

    speak("Command not recognized. Try: 'time', 'open YouTube', 'search for cats', 'play shape of you', or 'Wikipedia Sachin Tendulkar'.")
    return True

def main():
    speak("Voice command ready. Say a command, or say exit to quit.")
    while True:
        cmd = listen()
        if not handle_command(cmd):
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
