__author__ = 'matthias'
import colorsys
import random
import time

from light_schemes.application import Application


class Color(Application):
    name = 'color'
    color = 0, 0, 0

    def set_arguments(self, arguments):
        self.color = arguments.red, arguments.green, arguments.blue

    def set_options(self, options):
        if 'color' in options:
            self.color = tuple(map(int, options['color'].split(':')))

    @staticmethod
    def populate_parser(parser):
        parser.add_argument('red', type=int)
        parser.add_argument('green', type=int)
        parser.add_argument('blue', type=int)

    def run(self):
        self.manager.color(self.manager.all(), self.color)
        while self.running.is_set():
            time.sleep(0.5)