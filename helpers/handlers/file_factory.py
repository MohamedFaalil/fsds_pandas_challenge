from helpers.utilities.logger_utility import LogUtility
from helpers.utilities.file_utility import FileUtility
from helpers.handlers.doc_handler import DocHandler
from helpers.handlers.docx_handler import DocxHandler
from helpers.handlers.pdf_handler import PdfHandler


class FileFactory:
    @staticmethod
    def get_file(file_path):
        try:
            if FileUtility.get_file_extension(file_path) == '.docx':
                return DocxHandler(file_path)
            elif FileUtility.get_file_extension(file_path) == '.doc':
                return DocHandler(file_path)
            elif FileUtility.get_file_extension(file_path) == '.pdf':
                return PdfHandler(file_path)
            else:
                raise Exception("Incompatible file format.")
        except Exception as ex:
            LogUtility.write_error('factory.log',
                                   "Exception occurred, while getting  file object of the path `{}` (->on FileFactory=>get_file()<-) : {}".format(
                                       file_path, str(ex)))
            raise Exception(ex)
