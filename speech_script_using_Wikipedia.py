
import pyttsx3
import wikipedia
import speech_recognition as sr

engine = pyttsx3.init()

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Talk...")
    audio_text = r.listen(source)
    print("Done.")
   
    try:
        sa = r.recognize_google(audio_text)
        # print("Text: "+r.recognize_google(audio_text))
    except:
        print("Sorry, I did not get that")

result = wikipedia.summary(sa, sentences = 2)
print(result)

engine.say(result)
engine.say("Thank you, sir")
engine.runAndWait()