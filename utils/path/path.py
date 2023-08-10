import os
import random


class Path:

    @staticmethod
    def get_current_working_directory():
        return os.getcwd()

    @staticmethod
    def create_path_for_necessary_folder(current_directory, target_folder_name):
        return os.path.join(current_directory, target_folder_name)

    @staticmethod
    def get_folder_path(folder_name):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(current_dir, folder_name)

    @staticmethod
    def get_random_files_from_folder(folder_path, num_files=1):
        file_names = os.listdir(folder_path)
        # Exclude '__init__.py' files
        file_names = [file_name for file_name in file_names if file_name != "__init__.py"]
        if len(file_names) <= num_files:
            return file_names
        else:
            random_files = random.sample(file_names, num_files)
            return random_files
