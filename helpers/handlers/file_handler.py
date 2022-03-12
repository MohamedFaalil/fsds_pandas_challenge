import re

from abc import ABC, abstractmethod


class FileHandler(ABC):
    ###############################################################################################################
    ################################## ----- PUBLIC METHODS ----##################################################
    ###############################################################################################################
    def __init__(self, document_text, messed_str_pattern_list):
        self.document_text = document_text
        self.__get_messed_str_pattern_list = messed_str_pattern_list

    def get_mail_address(self):
        pattern_list = self.__get_mail_address_pattern()
        return self.__get_matched_links(self.document_text, pattern_list)

    def get_linked_in_address(self):
        pattern_list = self.__get_linked_in_link_pattern()
        return self.__get_matched_links(self.document_text, pattern_list)

    def get_git_repository_address(self):
        pattern_list = self.__get_git_repository_link_pattern()
        return self.__get_matched_links(self.document_text, pattern_list)

    ###############################################################################################################
    ################################## ----- ABSTRACT METHODS ----##################################################
    ###############################################################################################################
    @abstractmethod
    def get_skills(self):
        pass

    ###############################################################################################################
    ################################## ----- PRIVATE METHODS ----##################################################
    ###############################################################################################################
    @staticmethod
    def __get_git_repository_link_pattern():
        return [
            '''https?:\/{2}github\.com\/\w*'''
        ]

    @staticmethod
    def __get_linked_in_link_pattern():
        return [
            '''w{3}\.linkedin\.com\/in\/[\w-]*'''
        ]

    @staticmethod
    def __get_mail_address_pattern():
        return [
            '''[\w\.\_]*\@.*\.com'''
        ]

    def __get_matched_links(self, text, pattern_list):
        links = ''
        for pattern in pattern_list:
            match = re.findall(pattern, text, re.MULTILINE | re.IGNORECASE)
            if match is None:
                continue
            matched_str =     self._get_cleared_string(match)
            links += "{link} ".format(link=matched_str)
        return links

    def _get_cleared_string(self, match_list):
        match_list = list(set(match_list))
        txt = ''
        for match in match_list:
            txt += ' ' + match
        for pattern in self.__get_messed_str_pattern_list:
            txt = re.sub(pattern, '', txt)
        return txt
