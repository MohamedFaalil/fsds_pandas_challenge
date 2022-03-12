import win32com.client as win_client

from helpers.utilities.logger_utility import LogUtility
from helpers.handlers.document import Document


class DocHandler(Document):
    def __init__(self, file_path):
        try:
            document_text = self.__read_document(file_path)
            super(DocHandler, self).__init__(document_text)
        except Exception as ex:
            LogUtility.write_error('document.log',
                                   "Exception occurred, while reading file `{}` (->on DocHandler=>__init__()<-) : {}".format(
                                       file_path, str(ex)))
            raise Exception("could not able to read file `{}`".format(file_path))

    def __read_document(self, path):
        word = win_client.Dispatch("Word.Application")
        word.visible = False
        word.Documents.Open(path)
        doc = word.ActiveDocument
        txt = doc.Range().Text
        word.Application.Quit()
        return txt
