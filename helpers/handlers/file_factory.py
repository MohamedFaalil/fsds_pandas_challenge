from helpers.utilities.file_utility import FileUtility


class FileFactory:
    @staticmethod
    def get_file(file_path):
        try:
            if FileUtility.get_file_extension(file_path) == '.docx':
                pass
            elif FileUtility.get_file_extension(file_path) == '.doc':
                pass
            elif FileUtility.get_file_extension(file_path) == '.pdf':
                pass
        except Exception as ex:
            raise Exception(ex)
