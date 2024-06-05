import io
import threading

from time import sleep
from queue import Queue
import speech_recognition as sr
from datetime import datetime, timedelta

from Agent.IO.Output.Translation import translate_text
from Agent.Utils.SaveFile import save_audio, save_transcription
from Agent.Utils.ReadSettings import create_data_folder
from Agent.IO.Input.Input import get_source_recoder, capture_and_save_audio_background, speech_to_text

data_buffer = Queue()


def generate_transcription(source, last_sample):
    audio_data = sr.AudioData(last_sample, source.SAMPLE_RATE, source.SAMPLE_WIDTH)
    wav_data = io.BytesIO(audio_data.get_wav_data())

    file_path = save_audio(wav_data)

    transcription = speech_to_text(file_path)
    translation = translate_text(transcription)
    save_transcription(transcription, "User")
    return transcription, translation

def transcription_loop(source, phrase_timeout):
    global data_buffer
    last_sample = bytes()
    phrase_time = None
    transcription_history = []
    translate_history = []

    prev_transcription = ""
    prev_translation = ""

    while True:
        # print("transcription_history", transcription_history)
        now = datetime.utcnow()
        try:
            now = datetime.utcnow()
            if not data_buffer.empty():
                if (phrase_time and now - phrase_time >  timedelta(seconds=phrase_timeout)):
                    prev_transcription = prev_transcription.strip('\n')
                    prev_translation = prev_translation.strip('\n')
                    transcription_history.append(prev_transcription)
                    translate_history.append(prev_translation)
                    last_sample = bytes()

                phrase_time = now

                while not data_buffer.empty():
                    data = data_buffer.get()
                    last_sample += data
                
                transcription, translation = generate_transcription(source, last_sample)
                prev_transcription = transcription
                prev_translation = translation

                print("transcription:", (" ").join(transcription_history) + transcription)
                print("translation:", (" ").join(translate_history) + translation)
        
        except KeyboardInterrupt:
            break
            
        sleep(1)

def start_recording():
    global data_buffer
    source, recorder, record_timeout, phrase_timeout, pause_threshold = get_source_recoder()
    stop_listening = capture_and_save_audio_background(data_buffer, source, recorder, record_timeout)
    threading.Thread(target=transcription_loop, args=(source,phrase_timeout)).start()

if __name__ == '__main__':
    create_data_folder()
    start_recording()

