__author__ = 'matthias'


import time

import serial


class InvalidColor(Exception):
    pass


def test_color(color):
    return 0 <= color < 256


class Color:
    """
    :param stripe:
    :param red:
    :param green:
    :param blue:
    """
    def __init__(self, stripe, red, green, blue):
        self._stripe = stripe
        if test_color(red):
            self._red = red
        else:
            raise InvalidColor
        if test_color(green):
            self._green = green
        else:
            raise InvalidColor
        if test_color(blue):
            self._blue = blue
        else:
            raise InvalidColor


    @property
    def red(self):
        return self._red

    @red.setter
    def red(self, value):
        if test_color(value):
            self._stripe.color = (value, self._green, self._blue)
        else:
            raise InvalidColor

    def private_red_setter(self, value):
        if test_color(value):
            self._red = value
        else:
            raise InvalidColor



    @property
    def green(self):
        return self._green

    @green.setter
    def green(self, value):
        if test_color(value):
            self._stripe.color = (self._red, value, self._blue)
        else:
            raise InvalidColor

    def private_green_setter(self, value):
        if test_color(value):
            self._green = value
        else:
            raise InvalidColor

    @property
    def blue(self):
        return self._blue

    @blue.setter
    def blue(self, value):
        if test_color(value):
            self._stripe.color =(self._red, self._green, value)
        else:
            raise InvalidColor

    def private_blue_setter(self, value):
        if test_color(value):
            self._blue = value
        else:
            raise InvalidColor


class Stripe:
    """
    :param number:
    :param color:
    :param manager:
    """
    def __init__(self, number, color, manager):
        self._number = number
        self._red, self._green, self._blue = color
        self._color = Color(self, self._red, self._green, self._blue)
        self._manager = manager

    @property
    def color(self):
        return self._color

    def private_color_setter(self, color):
        self._red, self._green, self._blue = color
        self._color.private_red_setter(self._red)
        self._color.private_green_setter(self._green)
        self._color.private_blue_setter(self._blue)

    @color.setter
    def color(self, color):
        self.private_color_setter(color)
        self._manager.private_color_setter(color)




class Manager:
    """
    :param serial_interface_name: maby /dev/ttyACM=
    :param quantity_of_stripes:Number of stripes
    """
    def __init__(self, serial_interface_name, quantity_of_stripes):
        self._serial_interface_name = serial_interface_name
        self._dev = serial.Serial(self._serial_interface_name, 115200)
        self._quantity_of_stripes = quantity_of_stripes
        self._stripe_list =[]
        for i in range(quantity_of_stripes):
            self._stripe_list.append(Stripe(i, (0, 0, 0), self))
        #self._dev.setDTR(0)
        time.sleep(1)

    def private_color_setter(self, mask, color):
        """
        :param mask:
        :param color: 
        """
        _red, _green, _blue = color
        self._dev.write(bytes([mask, _red, _green, _blue]))


    def color(self, mask, color):
        _red, _green, _blue = color
        for i in range(self._quantity_of_stripes):
            num = mask & (1 << i)
            if num != 0:
                self._stripe_list[i].private_color_setter(color)
        self.private_color_setter(mask, color)

    def all(self):
        result=0
        for i in range(self._quantity_of_stripes):
            result |= (1 << i)
        return result
