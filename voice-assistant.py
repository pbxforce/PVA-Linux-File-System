import speech_recognition as sr
import webbrowser as browser
import os
import playsound
import random
from gtts import gTTS
import time
from time import ctime


r = sr.Recognizer()


def convert(string):
    li = list(string.split(" "))
    return li


def recorded_audio_data(ask=False):
    with sr.Microphone() as source:
        if ask:
            audio_data(ask)
        audio_input = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio_input)
        except sr.UnknownValueError:
            audio_data("Sorry, i didn't get that clearly.")
        except sr.RequestError():
            audio_data("Sorry, speech service is down.")
        return voice_data


def response(voice_data):
    if 'what is your name' in voice_data:
        audio_data("I am the nameless.")
    if 'what time is it' in voice_data:
        audio_data(ctime())
    if 'search' in voice_data:
        voice_data_list = convert(voice_data)
        voice_data_popped = voice_data_list.pop(0)
        voice_str = " ".join(voice_data_list)
        url = 'https://google.com/search?q=' + voice_str
        browser.get().open(url)
        audio_data("Here are the results for: " + voice_str)
    if 'movie' in voice_data:
        voice_data_list = convert(voice_data)
        voice_data_popped = voice_data_list.pop()
        voice_str = " ".join(voice_data_list)
        url1 = 'https://vegamovies.show/?s=' + voice_str
        url2 = 'https://pahe.li/?s=' + voice_str
        browser.get('google-chrome').open(url1)
        browser.get('google-chrome').open(url2)
        audio_data("Here are the results for: " + voice_str)
    if 'torrent' in voice_data:
        voice_data_list = convert(voice_data)
        voice_data_popped = voice_data_list.pop()
        voice_str = " ".join(voice_data_list)
        url = 'https://www.1377x.to/search/' + voice_str + '/1/'
        browser.get('google-chrome').open(url)
        audio_data("Here are the results for: " + voice_str)
    if 'terminate' in voice_data:
        audio_data("terminating on command")
        exit()


def audio_data(audio_string):
    tts = gTTS(text=audio_string, lang='en', slow=False)
    rn = random.randint(1, 1000000000)
    audio_file = 'audio-' + str(rn) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


time.sleep(0.5)
audio_data("i am listening...")
while 0.5:
    voice_data = recorded_audio_data()
    response(voice_data)
