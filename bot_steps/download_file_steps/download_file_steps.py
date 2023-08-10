import allure


class DownloadFileSteps:

    @staticmethod
    def download_file(bot, file_id):
        with allure.step("Get info about file using bot.get_file"):
            file_info = bot.get_file(file_id)

        with allure.step("Download the file using bot.download_file and file_info.file_path"):
            downloaded_file = bot.download_file(file_info.file_path)

        with allure.step("Doing unique file name: id file + file_info.file_path"):
            filename = file_id + file_info.file_path

        with allure.step("file_info.file_path looks like voice/file_123.oga, for ignoring errors we change / to _"):
            filename = filename.replace('/', '_')

        with open(filename, 'wb') as f:
            f.write(downloaded_file)

        return filename
