import os
from helpers.utilities.logger_utility import LogUtility


class FolderUtility:
    @staticmethod
    def get_folder_content_list(folder_path):
        try:
            return os.listdir(folder_path)
        except Exception as ex:
            LogUtility.write_error('folder-utility.log',
                                   "Folder '{}' content reading is failed. (->on FolderUtility=>get_folder_content_list()<-) : {}".format(
                                       folder_path, str(ex)))
            raise Exception('could not able to get folder contents')
