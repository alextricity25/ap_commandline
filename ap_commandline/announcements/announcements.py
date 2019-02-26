import requests
import argparse

class AnnouncementsClass():

    def __init__(self, subparser, client):
        self.subparser = subparser

    def get_parser(self):
        return self.subparser.add_parser(
                   'announcements',
                    help = "Subcommand for manipulating announcements"
               )
