import speech_recognition as sp
import pyttsx3
import unicodedata

def quitartildes(texto):
    texto_nfd = unicodedata.normalize('NFD', texto)
    texto_sin_tildes = ''.join(
        c for c in texto_nfd if unicodedata.category(c) != 'Mn'
    )
    return texto_sin_tildes

motor = pyttsx3.init('espeak')


voices = motor.getProperty('voices')
for voice in voices:
    if "spanish" in voice.name.lower() or "español" in voice.name.lower():
        motor.setProperty('voice', voice.id)
        break

def speak(texto):
    textonorm = quitartildes(texto)
    motor.say(textonorm)
    motor.runAndWait()


listener = sp.Recognizer()
mic = sp.Microphone()

with mic as source:
    print("Di algo...")
    listener.adjust_for_ambient_noise(source) 
    audio = listener.listen(source)

try:
    text = listener.recognize_google(audio, language='es-ES')
    print(f'Has dicho: {text}')
    speak(text)



except sp.UnknownValueError:
    print("No entendí lo que dijiste.")
