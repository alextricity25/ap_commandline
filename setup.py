import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "ap_commandline",
    version = "0.0.1a1",
    author = "Miguel Alex Cantu",
    author_email = "miguel.can2@gmail.com	",
    description = ("A command line tool for interacting with AP server"),
    license = "GNU General Public License v3 or later (GPLv3+)",
    keywords = "AP",
    packages=[
        'ap_commandline',
        'ap_commandline.announcements'
    ],
    install_requires = ['requests'],
    long_description=read('README.rst'),
    url = 'https://github.com/alextricity25/ap_commandline',
    download_url = 'https://github.com/alextricity25/ap_commandline/archive/0.0.1a1.tar.gz',
    entry_points = {
        'console_scripts': [
            'ap_commandline = ap_commandline.main:main'
        ]
    }
    
)
