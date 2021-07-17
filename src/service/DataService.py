from constants.constants import DEFAULT_FILE_NAME
import sys
import os
import json
import random


class DataService:
    '''
    Data service
    '''
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

    def random(self):
        word = random.choice(list(self.__data))
        return (word, self.__data[word])