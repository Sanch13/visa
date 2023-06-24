from pydub import AudioSegment
import argparse
from tkinter import Tk, filedialog


def convert_mp3_to_wav(mp3_file, wav_file):
    # Загрузка аудиофайла MP3
    audio = AudioSegment.from_mp3(mp3_file)

    # Сохранение аудиофайла в формате WAV
    audio.export(wav_file, format="wav")

    print("Преобразование завершено.")


def choose_file():
    # Создание экземпляра окна Tkinter
    root = Tk()
    root.withdraw()

    # Открытие диалогового окна выбора файла MP3
    mp3_file = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])

    if mp3_file:
        # Генерация пути для сохранения WAV-файла
        wav_file = mp3_file.replace(".mp3", ".wav")

        # Вызов функции для преобразования MP3 в WAV
        convert_mp3_to_wav(mp3_file, wav_file)

        print(f"Файл {mp3_file} успешно преобразован в {wav_file}")
    else:
        print("Выбор файла отменен.")


if __name__ == "__main__":
    choose_file()
