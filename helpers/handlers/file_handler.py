from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def get_mail_address(self):
        pass

    @abstractmethod
    def get_linked_in_address(self):
        pass

    @abstractmethod
    def get_git_repository_address(self):
        pass

    @abstractmethod
    def get_skills(self):
        pass

    @staticmethod
    def _get_git_repository_link_pattern():
        return [
            '''https?:\/{2}github\.com\/\w*'''
        ]

    @staticmethod
    def _get_linked_in_link_pattern():
        return [
            '''w{3}\.linkedin\.com\/in\/[\w-]*'''
        ]

    @staticmethod
    def _get_mail_address_pattern():
        return [
            '''[\w\.\_]*\@.*\.com'''
        ]
