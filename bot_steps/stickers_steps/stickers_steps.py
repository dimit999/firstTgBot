from utils.path.path import Path


class StickerSteps:

    @staticmethod
    def get_sticker(num_files=1):
        stickers_path = StickerSteps.get_stickers_path()
        random_file = Path.get_random_files_from_folder(stickers_path, num_files=num_files)
        if num_files == 1:
            return random_file[0]

    @staticmethod
    def get_stickers_path():
        main_file_path = Path.get_current_working_directory()
        return Path.create_path_for_necessary_folder(main_file_path, "stickers")
