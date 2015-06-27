# -*- coding:utf-8 -*-
#
# Copyright (C) 2015, Matthias Heerde <matthias.heerde@web.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import colorsys
import random
import time

from light_schemes.application import Application
from light_controlles import utils


class Strobe(Application):
    name = 'strobe'
    frequency = 10
    color = None
    all = False

    def set_arguments(self, arguments):
        self.frequency = arguments.frequency
        self.color = arguments.color
        self.all = arguments.all

    def set_options(self, options):
        if 'frequency' in options:
            self.frequency = int(options['frequency'])
        if 'color' in options:
            self.color = tuple(map(int, options['color'].split(':')))
        if 'all' in options:
            self.all = True

    @classmethod
    def populate_parser(cls, parser):
        parser.add_argument('-f', '--frequency', type=int,
                            default=cls.frequency)
        parser.add_argument('-c', '--color', type=int, nargs=3,
                            metavar=('RED', 'GREEN', 'BLUE'))
        parser.add_argument('-a', '--all', action='store_true')

    def run(self):
        max_mask = 2 ** self.manager._quantity_of_stripes - 1
        while self.running.is_set():
            if self.all:
                mask = self.manager.all()
            else:
                mask = random.randint(1, max_mask)
            if self.color:
                self.manager.color(mask, self.color)
            else:
                self.manager.color(mask, utils.random_color())
            time.sleep(1 / self.frequency)
            self.manager.color(self.manager.all(), (0, 0, 0))
            time.sleep(1 / self.frequency)