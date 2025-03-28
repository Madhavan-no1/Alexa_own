import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)  # Adjust for background noise
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'habibi' in command:
                command = command.replace('habibi', '')
                print(f'I heard: "{command}"')
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except sr.UnknownValueError:
        print("Could not understand audio, please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return command

def run_habibi():
    command = take_command()
    
    # If no command was captured, do not proceed
    if not command:
        return

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache, but lets have coffee togeather?')
    elif 'are you single' in command:
        talk('I am in a relationship with Maddhavan so sorry my deaar..')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'i love you' in command:
        talk("i love you too my lovely baby")
    else:
        talk('Please say the command again.')

if __name__ == "__main__":
    while True:
        run_habibi()
