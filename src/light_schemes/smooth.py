__author__ = 'matthias'

import colorsys
import time
from light_schemes.application import Application


class Smooth(Application):
    name = 'smooth'

    def run(self):
        hsv = 0
        while self.running.is_set():
            if hsv >= 1:
                hsv = 0
            hsv += (1 / 720)
            r, g, b = colorsys.hsv_to_rgb(hsv,  1, 1)
            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)
            #mask = self.manager.all()
            self.manager.color(0b11111, (r, g, b))
            time.sleep(0.2)



