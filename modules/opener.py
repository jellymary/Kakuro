import os.path as path


class Opener:
    @staticmethod
    def open_file(name):
        try:
            file_path = path.join('modules', 'fields', name)
            with open(str(file_path), 'r', encoding='UTF-8') as file:
                return file.readlines()
        except FileNotFoundError:
            print('invalid name of kakuro entered')
