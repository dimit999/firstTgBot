import allure
from pydub import AudioSegment


class FormatChanges:

    @staticmethod
    def oga2wav(oga_filename):
        with allure.step("Change format: 'sample.oga' -> 'sample.wav'"):
            new_filename = oga_filename.replace('.oga', '.wav')
        with allure.step("Read file from disk with AudioSegment.from_file()"):
            audio = AudioSegment.from_file(oga_filename)
        with allure.step("Export file with new format"):
            audio.export(new_filename, format='wav')

        return new_filename
