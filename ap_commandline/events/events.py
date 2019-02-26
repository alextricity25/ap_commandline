import requests
import argparse
import json
import pdb
import pprint

class EventsClass():

    def __init__(self, subparser, client):
        self.subparser = subparser
        self.client = client

    def get_parser(self):

        event_parser = self.subparser.add_parser(
                           'events',
                           help = "Subcommand for manipulating events")

        event_parser.add_argument(
            'context',
            action = 'store_const',
            const = 'events'
        ) 

        # The subcommands which define actions that can be performed against
        # events are defined here
        ## List action - Lists events
        event_subparser = event_parser.add_subparsers()
        list_parser = event_subparser.add_parser('list', help="List Events")
        self._build_arguments(list_parser, "list")

        ## generate_calendar - Generates an ics file with current events
        cal_parser = event_subparser.add_parser(
                         'generate_calendar',
                          help = "Generate an ICS file with all current events")
        self._build_arguments(cal_parser, "generate_calendar")

       

        return event_parser

    def _build_arguments(self, parser, action_name):
        """
        This method add's all the arguments related to this subparser
        """

        parser.add_argument(
            'action',
            action = 'store_const',
            const = action_name)


    def list(self):
        res = self.client.get("http://127.0.0.1:8000/api/events/")
        pprint.pprint(res.json())
        print "hi list!!"

    def generate_calendar(self):
        print "Generating Calendar!!!"
