import os

import allure
import telebot

from bot_steps.download_file_steps.download_file_steps import DownloadFileSteps
from bot_steps.recognize_speech_steps.recognize_speech_steps import BotRecognitionSteps
from bot_steps.stickers_steps.stickers_steps import StickerSteps
from bot_steps.transform_image.transform_image_steps import TransformImageSteps

with allure.step("BOT token"):
    token = '6535391532:AAFB5ELY238SzJTX9EyuP4MBgfGmd6EhR-I'

with allure.step("Take bot and give him remember token"):
    bot = telebot.TeleBot(token)

with allure.step("Function with answer to '/start' command, all functions for communication with telegram are under @"):
    @bot.message_handler(commands=['start'])
    def say_hi(message):
        bot.send_message(message.chat.id, 'Hello, {}!'.format(message.chat.username))


@bot.message_handler(commands=['sendsticker'])
def send_sticker(message):
    file_name = StickerSteps.get_sticker()
    chat_id = message.chat.id
    sticker_path = "{}/{}".format(StickerSteps.get_stickers_path(), file_name)

    bot.send_sticker(chat_id=chat_id, sticker=open(sticker_path, 'rb'))


with allure.step("New condition for catching content_types=['voice']"):
    @bot.message_handler(content_types=['voice'])
    def transcript(message):
        with allure.step("id file - in message.voice.file_id"):
            file_id = message.voice.file_id

        with allure.step("Download file"):
            filename = DownloadFileSteps.download_file(bot, file_id)
        with allure.step("Recognition record using recognize_speech function"):
            text = BotRecognitionSteps.recognize_speech(filename, language='ru')

        with allure.step("Send to user text answer"):
            bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['photo'])
def resend_photo(message):
    with allure.step("Resend updated image"):
        file_id = message.photo[-1].file_id
        filename = DownloadFileSteps.download_file(bot, file_id)

    with allure.step("Transform image"):
        TransformImageSteps.transform_image(filename)

    image = open(filename, 'rb')
    bot.send_photo(message.chat.id, image)
    image.close()

    with allure.step("Remove image"):
        if os.path.exists(filename):
            os.remove(filename)


with allure.step("RUN BOT. Bot will work until will work this function"):
    bot.polling()
