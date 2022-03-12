from abc import ABC
import re

from helpers.handlers.file_handler import FileHandler


class Document(FileHandler):
    def __init__(self, document_text):
        self.document_text = document_text
        super(Document, self).__init__(document_text, self.__get_messed_str_patterns())

    ###############################################################################################################
    ################################## ----- PUBLIC METHODS ----###################################################
    ###############################################################################################################

    def get_skills(self):
        pattern_dict = self.__skill_patterns()
        skills = ''
        for key in pattern_dict.keys():
            pattern = pattern_dict[key]
            match = re.findall(pattern, self.document_text, re.MULTILINE | re.IGNORECASE)
            if match is None:
                continue
            skills_str = self._get_cleared_string(match)
            skills += "{skill_key} => {skill} ".format(skill_key=key, skill=skills_str)
        return skills

    ###############################################################################################################
    ################################## ----- PRIVATE METHODS ----##################################################
    ###############################################################################################################

    def __skill_patterns(self):
        return {
            'programming_languages': '''Programming Languages\:\s*(.*)\s*(?:TOOLS|Knowledge In Technology)''',
            'database': '''Data Base\:\s*(.*)''',
            'coding_skills': '''CODING SKILLS\s*([\w\s\,\/]*)Experience''',
            'machine_learning': '''Machine learning\s*(?:Exposure to)?([\w\,\s\(\)]*)(?:Deep Learning|OTHER SKILLS)''',
            'other_skills': '''OTHER SKILLS\s*([\w\s\,\/]*)Experience''',
            'programming_skills': """Programming\s?\/Scripting\s*([\w\,]*)""",
            'data_science': '''Data Science\s*([\w\s\,-]*)Operating system''',
            'tools_capability': '''(?:Tools\:?\s?|\/IDE\s*)([\w\,\s\-]*)(?:Data Science|Cloud|Data Base)''',
            'operating_system': '''Operating system(?:s|\:)?\s+(.*)\s*(?:PROFESSIONALEXPERIENCE|Distribution|Programming)''',
            'key_skills_and_certifications': '''Key Skills \&  Certifications \:\s*([.\w\s\,\-\(\)\&]*)''',
            'domains': '''Domain\s*([\w\s]*)Programming''',
            'cloud': '''Cloud\s*([\w\,\s\(\)]*?)Machine learning''',
            'deep_learning': '''Deep Learning\/Computer vision\s*(.*)''',
            'project_methodology': '''Project Methodology\s*(.*)''',
            'distribution': '''Distribution\s*([\w\,\s]*)Hardware''',
            'hardware': '''Hardware\s*([\w\,\s\+]*)Version Control''',
            'version_control': '''Version Control\s*([\w\,\s\+]*)Professional Experience ''',
            'computer_vision': '''vision\s*(.*)''',
            'knowledge_in_technology': """Knowledge In Technology:(.*?)Projects"""
        }

    def __get_messed_str_patterns(self):
        return [
            "\n*",
        ]
