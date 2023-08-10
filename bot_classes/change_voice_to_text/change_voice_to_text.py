import speech_recognition


class VoiceToText:

    @staticmethod
    def speech_recognition(wav_file_name, language='ru'):
        recognizer = speech_recognition.Recognizer()

        with speech_recognition.WavFile(wav_file_name) as source:
            wav_audio = recognizer.record(source)

        return recognizer.recognize_google(wav_audio, language=language)


