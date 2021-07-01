import re
import sys
import json
import os

PUT_REGEX = '^\\s*put\\s+([^\\s])+\\s+([^\\s])+.*$'
GET_REGEX = '^\\s*get\\s+([^\\s])+.*$'
DELETE_REGEX = '^\\s*del\\s+([^\\s])+.*$'

DEFAULT_FILE_NAME = 'vocabulary.json'


class Main:
    def __init__(self, controller, file_name=DEFAULT_FILE_NAME):
        self.__fileName = file_name
        self.__controller = controller

    def run(self):
        try:
            while True:
                cmd = input(">> ")
                if re.match("exit", cmd, re.I):
                    print("\nAuto saving...")
                    self.__controller.save()
                    print("Bye!")
                    sys.exit(0)

                elif re.match("save", cmd, re.I):
                    print(self.__controller.save())

                elif re.match("list", cmd, re.I):
                    print(self.__controller.listKeys())

                elif re.match(PUT_REGEX, cmd, re.I):
                    items = re.split('\\s+', cmd, maxsplit=2)
                    word = items[1]
                    definition = items[2]
                    print(self.__controller.put(word, definition))

                elif re.match("put", cmd, re.I):
                    phrase = input(">> Enter phrase: ")
                    definition = input(">> Enter definition: ")
                    print(self.__controller.put(phrase, definition))

                elif re.match(GET_REGEX, cmd, re.I):
                    word = re.split('\\s+', cmd, maxsplit=1)[1]
                    print(self.__controller.get(word))

                elif re.match(DELETE_REGEX, cmd, re.I):
                    word = re.split('\\s+', cmd, maxsplit=1)[1]
                    print(self.__controller.delete(word))

                else:
                    if self.__controller.has_key(cmd):
                        print(self.__controller.get(cmd))
                    else:
                        print("Unknown cmd: '{}'".format(cmd))
                print()
        except KeyboardInterrupt:
            print("\nAuto saving...")
            print("Shuting down...")
            self.__controller.save()
            print("Bye!")
            sys.exit(0)


class Controller:
    def __init__(self, data_service, file_name=DEFAULT_FILE_NAME):
        self.__data_service = data_service
        self.__file_name = file_name

    def set_file_name(self, file_name):
        self.__file_name = file_name

    def put(self, key, value):
        return self.__data_service.put(key, value)

    def has_key(self, key):
        return self.__data_service.has_key(key)

    def get(self, key):
        if self.__data_service.has_key(key):
            return self.__data_service.get(key)
        return "word '{}' not in dictionary".format(key)

    def delete(self, key):
        return self.__data_service.delete(key)

    def save(self):
        return self.__data_service.save()

    def list_keys(self):
        return self.__data_service.list()


class DataService:
    def __init__(self, file_name=DEFAULT_FILE_NAME):
        self.__data = {}
        self.__file_name = file_name
        try:
            filePath = './data/' + file_name
            if not os.path.exists('./data'):
                print("Initializing data directory")
                os.mkdir("./data")
                print('Initializing dictionary...')
                with open(filePath, 'w') as file:
                    file.write('{}')
                    print('Initialization complete.')
            elif not os.path.exists(filePath):
                print('Initializing dictionary...')
                with open(filePath, 'w') as file:
                    file.write('{}')
                    print('Initialization complete.')
            else:
                with open(filePath, 'r') as file:
                    print("Start reading vocabularies...")
                    self.__data = json.load(file)
                    print("Loaded {} word(s).".format(len(self.__data)))
                    print("Dictionary ready!\n")

        except Exception as e:
            print(e)
            sys.exit(0)

    def has_key(self, key):
        return key in self.__data

    def get(self, key):
        return self.__data[key]

    def delete(self, key):
        if not self.has_key(key):
            return "Key '{}' doesn't exist.".format(key)
        self.__data.pop(key)
        return "Success."

    def put(self, key, value):
        self.__data[key] = value
        return "Success."

    def save(self):
        try:
            with open('./data/' + self.__file_name, 'w') as fobj:
                json.dump(self.__data, fobj)
                return "Success."
        except Exception as e:
            return str(e)

    def list(self):
        res = "{} words total.\n\n".format(len(self.__data))
        for key in self.__data:
            res += "{}    {}\n".format(key, self.__data[key])
        return res


if __name__ == '__main__':
    Main(Controller(DataService())).run()
