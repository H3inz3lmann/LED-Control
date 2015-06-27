__author__ = 'matthias'

import argparse

from light_controlles import controller
import light_schemes

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', default='/dev/ttyACM0')

    subparsers = parser.add_subparsers(dest='program')

    for name, app in light_schemes.applications.items():
        sub_parser = subparsers.add_parser(name)
        app.populate_parser(sub_parser)

    arguments = parser.parse_args()

    if not arguments.program:
        parser.print_help()
        return

    manager = controller.Manager(arguments.device, 5)

    app = light_schemes.applications[arguments.program](manager)
    app.set_arguments(arguments)
    app.start()

if __name__ == '__main__':
    main()