import re
import sys

from constants.constants import *
from service.DataService import DataService
from controller.Controller import Controller


class Main:
    '''
    main class
    '''
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

                elif re.match("review", cmd, re.I):
                    print("review >> Press [Enter]: see the definition.\n" + 
                            "review >> Enter 'q' to exit.\n")
                    while True:
                        word, definition = self.__controller.review()
                        cmd = input( '"' + word + '" >> ')
                        if cmd == 'q':
                            break
                        else:
                            input('"' + definition + '"')
                            print()
                    print("\nReview session ends.\n")

                else:
                    if self.__controller.has_key(cmd):
                        print(self.__controller.get(cmd))
                    elif len(cmd.strip()) == 0:
                        pass
                    else:
                        print("Unknown cmd: '{}'".format(cmd))
                print()
        except KeyboardInterrupt:
            print("\nAuto saving...")
            print("Shuting down...")
            self.__controller.save()
            print("Bye!")
            sys.exit(0)


'''
Program entrance
'''
if __name__ == '__main__':
    Main(Controller(DataService())).run()
