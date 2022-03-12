import docx2txt
from helpers.utilities.logger_utility import LogUtility

from helpers.handlers.document import Document


class DocxHandler(Document):
    def __init__(self, file_path):
        try:
            document_text = docx2txt.process(file_path)
            super(DocxHandler, self).__init__(document_text)
        except Exception as ex:
            LogUtility.write_error('document.log',
                                   "Exception occurred, while reading file `{}` (->on DocxHandler=>__init__()<-) : {}".format(
                                       file_path, str(ex)))
            raise Exception("could not able to read file `{}`".format(file_path))

