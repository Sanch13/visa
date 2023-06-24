import vosk
import wave
import json
from pydub import AudioSegment

# url = "https://visa.vfsglobal.com/blr/en/pol/login"


def get_text_from_audio():
    """mp3 в текст"""
    """ Нужно скачать модель с сайта -> https://alphacephei.com/vosk/models
    Берем самую маленькую по объему модель.
    Нужно установить в систему -> sudo apt-get install ffmpeg"""

    """Загружаем модель"""
    model_path = "vosk-model-small-en-us-0.15"  # https://alphacephei.com/vosk/models
    vosk.SetLogLevel(-1)
    model = vosk.Model(model_path)

    """Открываем файл"""
    audio_file = "Track63.mp3"  # аудио для распознавания
    wav_file = "audio.wav"

    """Конвертируем в файл WAV"""
    audio = AudioSegment.from_mp3(audio_file)
    audio.export("audio.wav", format="wav")

    """Открываем WAV"""
    wf = wave.open(wav_file, "rb")

    """Объект распознавания речи"""
    rec = vosk.KaldiRecognizer(model, wf.getframerate())

    """Распознаем текст"""
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = rec.Result()
            print(result)
            result = json.loads(result)
            recognized_text = result["text"]
            print(recognized_text)
            return recognized_text


get_text_from_audio()
