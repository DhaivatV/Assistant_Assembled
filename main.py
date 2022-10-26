import json
import requests
import pyttsx3
import speech_recognition as sr
from API_CALL import query_api
import json
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    device_name = ("Aaruush")
    speak("I am your Assistant")
    speak(device_name)

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


def questionAns(path, question):
    with open(path) as file:
        lines = file.read()

    API_TOKEN = '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'
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"

    def query(payload):
        data = json.dumps(payload)
        response = requests.request("POST", API_URL, headers=headers, data=data)
        return json.loads(response.content.decode("utf-8"))

    data = query(
        {
            "inputs": {
                "question": question,
                "context": lines,
            }
        }
    )

    result = (data.get('answer'))
    return result


if __name__ == "__main__":

    while True:
        query = input("Enter Query:").lower()
        text_doc_list = (query_api(query)).text.split(":")
        text_doc = ((text_doc_list[1])[1:-2])+".txt"
        print(text_doc)
        print(questionAns(text_doc, query))
