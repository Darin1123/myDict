from constants.constants import DEFAULT_FILE_NAME


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

    def review(self):
        return self.__data_service.random()