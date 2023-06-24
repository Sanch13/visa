import speech_recognition as sr

r = sr.Recognizer()

audio_file = "audio.wav"

with sr.AudioFile(audio_file) as source:
    audio = r.record(source)


try:
    text = r.recognize_google(audio)
    print(text)
except sr.UnknownValueError:
    print("Не удалось распознать речь")
except sr.RequestError as e:
    print("Ошибка сервиса распознавания речи; {0}".format(e))

