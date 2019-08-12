"""
A program using speech recognition python to convert speech to text using the module
and then further using the text to open the url in web browser. Also searching the query using the speech in the URL
"""
import speech_recognition as spr
import webbrowser as web

rec1 = spr.Recognizer()
rec2 = spr.Recognizer()
rec3 = spr.Recognizer()


with spr.Microphone() as source:
    print('[search google : search youtube]')
    print('speak now')
    audio = rec3.listen(source)

if 'google' in rec2.recognize_google(audio):
    rec2 = spr.Recognizer()
    url = 'https://www.google.com/'
    with spr.Microphone() as source:
        print('search your query')
        audio = rec2.listen(source)

        try:
            get = rec2.recognize_google(audio)
            print(get)
            web.open_new(url+get)
        except spr.UnknownValueError:
            print('error')
        except spr.RequestError as e:
            print('failed'.format(e))

if 'youtube' in rec1.recognize_google(audio):
    rec1 = spr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with spr.Microphone() as source:
        print('search your query')
        audio = rec1.listen(source)

        try:
            get = rec1.recognize_google(audio)
            print(get)
            web.open_new(url+get)
        except spr.UnknownValueError:
            print('error')
        except spr.RequestError as e:
            print('failed'.format(e))
