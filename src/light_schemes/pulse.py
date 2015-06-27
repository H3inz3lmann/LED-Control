__author__ = 'matthias'

import time
from light_schemes.application import Application
from light_controlles import utils

class Pulse(Application):
    name = 'pulse'

    speed = 100
    color = None

    def set_arguments(self, arguments):
        self.speed = arguments.speed
        self.color = arguments.color

    @classmethod
    def populate_parser(cls, parser):
        parser.add_argument('-s', '--speed', type=int,
                            default=cls.speed)
        parser.add_argument('-c', '--color', type=int, nargs=3,
                            metavar=('RED', 'GREEN', 'BLUE'))


    def run(self):
        hue = 0
        while self.running.wait(0.1):
            hue = (hue % 360) + 10
            brightness = 0
            for i in range(51):
                if self.color:
                    color = utils.change_brightness(self.color,
                                                    brightness)
                else:
                    color = utils.hsv_to_rgb(hue, value=brightness)
                self.manager.color(0b11111, color)
                time.sleep(1 / self.speed)
                brightness += 2
            time.sleep(10 / self.speed)
            for i in range(51):
                brightness -= 2
                if self.color:
                    color = utils.change_brightness(self.color,
                                                    brightness)
                else:
                    color = utils.hsv_to_rgb(hue, value=brightness)
                self.manager.color(0b11111, color)
                time.sleep(1 / self.speed)
            time.sleep(10 / self.speed)