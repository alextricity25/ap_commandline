# Imports
from abc import ABCMeta, abstractmethod


# Classes

class BaseCredFetcher():

    def __init__(self):
        self.username = ""
        self.password = ""

    @abstractmethod
    def fetch_creds():
        """
        Every class in this package must inherit BaseCredFetcher and
        implement this method. The method fetches the credentials
        for a user's AP account depending on what module is being used
        to invoke this method.
        """
        pass
