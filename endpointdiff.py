import argparse
import subprocess

class bcolors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'

def get_endpoints(url, cookies, regex):
    endpoints = subprocess.Popen(['python3', 'LinkFinder/linkfinder.py', '-i', url, '-o', 'cli', '-c', cookies, '-r', regex], stdout=subprocess.PIPE)
    return [endpoint for endpoint in endpoints.stdout.read().decode('utf-8').split('\n') if endpoint]


def get_diff(old_endpoints, new_endpoints):
    removed = [endpoint for endpoint in old_endpoints if endpoint not in new_endpoints]
    added = [endpoint for endpoint in new_endpoints if endpoint not in old_endpoints]

    return removed, added


if __name__ == "__main__":
    # Parse command line
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--new",
                        help="Input a new: URL, file or folder. \
                        For folders a wildcard can be used (e.g. '/*.js').",
                        required=True, action="store")
    parser.add_argument("-o", "--old",
                        help="Input an old: URL, file or folder. \
                        For folders a wildcard can be used (e.g. '/*.js').",
                        required=True, action="store")
    parser.add_argument("-r", "--regex",
                        help="RegEx for filtering purposes \
                            against found endpoint (e.g. ^/api/)",
                        action="store", default="")
    parser.add_argument("-c", "--cookies",
                        help="Add cookies for authenticated JS files",
                        action="store", default="")
    parser.add_argument("-s", "--save",
                        help="File location to save the diff output to",
                        action="store")
    args = parser.parse_args()
    old_endpoints = get_endpoints(args.old, args.cookies, args.regex)
    new_endpoints = get_endpoints(args.new, args.cookies, args.regex)
    removed, added = get_diff(old_endpoints, new_endpoints)

    for endpoint in added:
        print(f'{bcolors.GREEN} + {endpoint} {bcolors.END}')

    for endpoint in removed:
        print(f'{bcolors.RED} - {endpoint} {bcolors.END}')

    if args.save:
        with open(args.save, 'w') as f:
            for endpoint in added:
                f.write(f'+ {endpoint}\n')
            for endpoint in removed:
                f.write(f'- {endpoint}\n')
