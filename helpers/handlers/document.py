from abc import ABC
import re

from helpers.handlers.file_handler import FileHandler


class Document(ABC, FileHandler):
    def __init__(self, document_text):
        self.document_text = document_text

    ###############################################################################################################
    ################################## ----- PUBLIC METHODS ----###################################################
    ###############################################################################################################

    def get_mail_address(self):
        pattern_list = self._get_mail_address_pattern()
        return self.__get_matched_links(self.document_text, pattern_list)

    def get_linked_in_address(self):
        pattern_list = self._get_linked_in_link_pattern()
        return self.__get_matched_links(self.document_text, pattern_list)

    def get_git_repository_address(self):
        pattern_list = self._get_git_repository_link_pattern()
        return self.__get_matched_links(self.document_text, pattern_list)

    def get_skills(self):
        pattern_dict = self.__skill_patterns()
        skills = ''
        for key in pattern_dict.keys():
            pattern = pattern_dict[key]
            match = re.findall(pattern, self.document_text, re.MULTILINE | re.IGNORECASE)
            if match is None:
                continue
            skills += "{skill_key}=> {skill} \n".format(skill_key=key, skill=self.__get_cleared_string(match))
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

    def __get_cleared_string(self, match_list):
        match_list = list(set(match_list))
        txt = ''
        for match in match_list:
            txt += ' ' + match
        for pattern in self.__get_messed_str_patterns():
            txt = re.sub(pattern, '', txt)
        return txt

    def __get_matched_links(self, text, pattern_list):
        links = ''
        for pattern in pattern_list:
            match = re.findall(pattern, text, re.MULTILINE | re.IGNORECASE)
            if match is None:
                continue
            links += "{link} ".format(self.__get_cleared_string(match))
        return links
