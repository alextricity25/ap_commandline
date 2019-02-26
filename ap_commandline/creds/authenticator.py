# Imports
import requests
from collections import OrderedDict
import pdb


# Classes

class APAuthenticator():

    def __init__(self, url = '127.0.0.1', port = '8000'):
        self.login_url = "http://{}:{}/accounts/login/".format(url, port)
        self.client = requests.session()
        self.client.get(self.login_url)
        self.csrftoken = self.client.cookies['csrftoken']

        # cred_precedence defines in what order the program will attempt
        # to load credentials. The right most entry in the OrdredDict will
        # always supercede the left most entry if available.
        cred_precedence = OrderedDict()
        cred_precedence['osenv'] = "OSEnvCredFetcher" 

        # Cycle through the CredFetcher classes to fetch username
        # and password. Stop when they are successfully retrieved.
        for cred_module_name, CredFetcherClass in cred_precedence.iteritems():
            # Import class
            cred_module = __import__('ap_commandline.creds.{}'.format(
                             cred_module_name),
                             fromlist = "blah")
            #pdb.set_trace()
            cred_class = getattr(cred_module, CredFetcherClass)
            self.login_data = cred_class().fetch_creds()
            if self.login_data['username'] and self.login_data['password']:
                break

        self.login_data['csrfmiddlewaretoken'] = self.csrftoken
        self.login_data['next'] = '/'
            

    def login(self):

        self.client.post(self.login_url, data = self.login_data)
        return self.client
