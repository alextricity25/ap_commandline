# Imports
import os
from ap_commandline.creds.base import BaseCredFetcher



# Classes

class OSEnvCredFetcher(BaseCredFetcher):

    def __init__(self):
        self.username = os.environ['FTTA_USERNAME']
        self.password = os.environ['FTTA_PASSWORD']

    def fetch_creds(self):
        """
        Return credentials that are stored in OS environment variables.
        """
        return { 'username': self.username, 
                 'password': self.password }
