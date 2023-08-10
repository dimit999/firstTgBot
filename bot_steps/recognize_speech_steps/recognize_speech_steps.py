import os

import allure

from bot_classes.change_voice_to_text.change_voice_to_text import VoiceToText
from bot_classes.format_changes.format_changes import FormatChanges


class BotRecognitionSteps:

    @staticmethod
    def recognize_speech(oga_filename, language='ru'):
        with allure.step("Modify format"):
            wav_filename = FormatChanges.oga2wav(oga_filename)

        with allure.step("Voice recognition"):
            text = VoiceToText.speech_recognition(wav_filename, language=language)

        with allure.step("Remove used voice files"):
            if os.path.exists(oga_filename):
                os.remove(oga_filename)

            if os.path.exists(wav_filename):
                os.remove(wav_filename)

        return text
