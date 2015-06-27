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


def hsv_to_rgb(hue, saturation=100, value=100):
    r, g, b = colorsys.hsv_to_rgb(hue / 360, saturation / 100,
                                  value / 100)
    return int(r * 255), int(g * 255), int(b * 255)


def random_color():
    return hsv_to_rgb(random.random() * 360)


def change_brightness(color, brightness=100):
    r, g, b = color
    fraction = brightness / 100
    return int(r * fraction), int(g * fraction), int(b * fraction)