import ffpicker.config as config
from ffpicker.data import fetch, transform

import argparse, json, logging

def parse_args():
    parser = argparse.ArgumentParser(description='Pick fantasy football winning team.')
    parser.add_argument('--log', dest='log_level', action='store',
                        default='warn', help='specify log level (default: warn)')
    return parser.parse_args()

def main():
    args = parse_args();
    logging.basicConfig(level=args.log_level.upper())

    configuration = config.Config()
    print(configuration.get_property("SCHEDULE_URL"))

    schedule = fetch.schedule(2017, 3)
    transform.schedule_xml_to_json(schedule)
    print(json.dumps(schedule.data, indent=2, sort_keys=True))

    fetch.game()

if __name__ == '__main__':
    main()
