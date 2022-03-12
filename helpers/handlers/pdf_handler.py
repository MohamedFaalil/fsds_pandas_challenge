import PyPDF2
import re


from helpers.utilities.file_utility import FileUtility
from helpers.utilities.logger_utility import LogUtility
from helpers.handlers.file_handler import FileHandler


class PdfHandler(FileHandler):
    def __init__(self, file_path):
        try:
            self.document_text = self.__read_pdf(file_path)
            super(PdfHandler, self).__init__(self.document_text, self.__get_messed_str_patterns())

        except Exception as ex:
            LogUtility.write_error('document.log',
                                   "Exception occurred, while reading file `{}` (->on DocxHandler=>__init__()<-) : {}".format(
                                       file_path, str(ex)))
            raise Exception("could not able to read file `{}`".format(file_path))

    def get_skills(self):
        pattern_list = self.__skill_patterns()
        skills = ''
        for pattern in pattern_list:
            match = re.findall(pattern, self.document_text, re.MULTILINE | re.IGNORECASE)
            if match is None:
                continue
            cleared_skill_txt =  self._get_cleared_string(match)
            skills += "{skill} ".format(skill=cleared_skill_txt)
        return skills

    def __read_pdf(self, path):
        file = FileUtility.get_readable_file_pointer(path)
        reader = PyPDF2.PdfFileReader(file)
        totalPage = reader.getNumPages()
        pageText = ''
        for pageNo in range(totalPage):
            if pageNo != 0:
                pageText += "\n"
            pageText += reader.getPage(pageNo).extractText()
        return pageText

    def __skill_patterns(self):
        return [
            '''Experience in years([\w\s\(\)\-\+\,\.\/\&\~]*)Achievements''',
            '''(?<=Core Competencies\s)+[\s\w\/]*(?=Nearly)''',
            '''Experience in Years([\w\s\(\)\-\+\,\.\/\&\~]*)RECOGNISIONS'''
        ]

    def __get_messed_str_patterns(self):
        return [
            "\n*",
            """\d+\s?\+\s*[yY]ears?""",
            """(Intermediate|Expert|Working Knowledge)"""
        ]
