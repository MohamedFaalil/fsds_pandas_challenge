from helpers.utilities.logger_utility import LogUtility
import os
import re


class FileUtility:
    @staticmethod
    def get_readable_file_pointer(file_location):
        try:
            if not os.path.exists(file_location) and not os.path.isfile(file_location):
                LogUtility.write_warning('file-processing.log',
                                         "File '{}' does not exist to read.".format(file_location))
                raise Exception("'{}' is not exists".format(file_location))

            return open(file_location, 'rb')
        except Exception as ex:
            LogUtility.write_error('file-util.log',
                                   "Exception occurred, while reading file `{}` (->on FileHandler=>__get_readable_file_pointer()<-) : {}".format(
                                       file_location, str(ex)))
            raise Exception("could not able to read file `{}`".format(file_location))

    @staticmethod
    def get_file_content_as_list(file_location):
        try:
            return FileUtility.get_readable_file_pointer(file_location).read().splitlines()
        except Exception as ex:
            LogUtility.write_error('file-util.log',
                                   "Exception occurred, while reading file `{}` (->on FileHandler=>get_file_content_as_list()<-) : {}".format(
                                       file_location, str(ex)))
            raise Exception("could not able to read and get file `{}` as list".format(file_location))

    @staticmethod
    def get_file_extension(file_path):
        pattern = '''^(?:.*)(\..*$)'''
        match = re.findall(pattern, file_path, re.MULTILINE | re.IGNORECASE)
        return match[0] if match is not None else ''
