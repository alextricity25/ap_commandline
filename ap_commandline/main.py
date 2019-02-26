# I should make a template for python scripts


# Imports
from ap_commandline.events.events import EventsClass
from ap_commandline.announcements.announcements import AnnouncementsClass
from ap_commandline.bible_tracker.bible_tracker import BibleTrackerClass
from ap_commandline.creds.authenticator import APAuthenticator
import argparse
import pdb


def main():


    parser = argparse.ArgumentParser(
        usage = '%(prog)s',
        description = "A Command Line tool for interfacing with the Attendance Server"
    )
    
    parser.add_argument(
        '-t',
        action = 'store_true',
        help = 'This is a test argument',
    ) 
    
    subparsers = parser.add_subparsers(
                     help = "sub-command help"
                 )

    client = APAuthenticator().login()

    # Map positional arguments with class names
    CLASS_MAPPINGS = {
        "events": {
            "class": EventsClass(subparsers, client),
            "subparser": None
        },
        "announcements": {
            "class": AnnouncementsClass(subparsers, client),
            "subparser": None
        },
        "bible_tracker": {
            "class": BibleTrackerClass(subparsers, client),
            "subparser": None
        }
    }

    # Populate subparsers
    for class_name, attrs in CLASS_MAPPINGS.iteritems():
        attrs["subparser"] = attrs['class'].get_parser()
    
    args = parser.parse_args()


    action_method = getattr(CLASS_MAPPINGS[args.context]['class'], args.action)
    action_method()
    #pdb.set_trace()


if __name__ == '__main__':
    main()
    
