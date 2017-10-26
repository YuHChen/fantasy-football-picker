import ffpicker.data.fetch as fetch
import ffpicker.pick as pick

import argparse, json, logging

def parse_args():
    parser = argparse.ArgumentParser(description='Pick fantasy football winning team.')
    parser.add_argument('--log', dest='log_level', action='store',
                        default='warn', help='specify log level (default: warn)')
    return parser.parse_args()

def main():
    args = parse_args();
    logging.basicConfig(level=args.log_level.upper())

    schedule = fetch.schedule(2017, 3)
    print(schedule)

    matches = [('giants', 'bears'), ('giants', 'seahawks'), ('bears', 'colts')]
    for match in matches:
        result = pick.between(*match).using(pick.team_bias).fallback(pick.random_team)
        print('The winner between [{}] and [{}] is [{}] because:'.format(*match, result.winner))
        print(result.reason)

if __name__ == '__main__':
    main()
