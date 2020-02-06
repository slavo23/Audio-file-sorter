import mutagen
import os
import shutil
import sys


class AudioFileSorter:
    __files_dict = {}

    def __init__(self, input_directory, output_directory, sort_criterion="TPE1"):
        self.input_directory = input_directory
        self.output_directory = output_directory
        self.sort_criterion = sort_criterion

    def __move_and_sort(self):
        files_count = 0
        for keys, path_array in self.__files_dict.items():
            if not keys in os.listdir(self.output_directory):
                subdir = os.path.join(self.output_directory, keys)
                subdir_path = os.path.join(self.output_directory, subdir)
                os.mkdir(subdir)
                for file_path in path_array:
                    shutil.move(file_path, subdir_path)
                    files_count += 1
        print(f"Successfully moved and sorted {files_count} files.")

    def __update_files_dict(self, field, audio_file_path):
        f_path = os.path.join(self.input_directory, audio_file_path)
        if not field in self.__files_dict:
            self.__files_dict[field] = []
            self.__files_dict[field].append(f_path)
        else:
            self.__files_dict[field].append(f_path)

    def read_files(self):
        for audio in os.listdir(self.input_directory):
            audio_path = os.path.join(self.input_directory, audio)
            if os.path.isdir(audio_path):
                continue
            with open(audio_path, "rb") as f:
                if mutagen.File(f) != None:
                    track = mutagen.File(f)
                    metadata_field = track[self.sort_criterion].text[0]
                    self.__update_files_dict(metadata_field, audio)
        self.__move_and_sort()


if __name__ == "__main__":
    in_path = input("Path to the unsorted music folder: ")
    out_path = input("Path to the output folder: ")
    AudioFileSorter(in_path, out_path).read_files()
