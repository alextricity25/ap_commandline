import requests
import argparse

class BibleTrackerClass():

    def __init__(self, subparser, client):
        self.subparser = subparser

    def get_parser(self):
        return self.subparser.add_parser(
                   'bible_tracker',
                   help = 'Subcommand for interacting with bible tracker'
               )
