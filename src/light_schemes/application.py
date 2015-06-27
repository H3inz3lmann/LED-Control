__author__ = 'matthias'

import threading


class MetaApplication(type):
    applications = {}

    def __new__(cls, name, bases, namespace, **kwargs):
        result = type.__new__(cls, name, bases, dict(namespace))
        if result.name:
            MetaApplication.applications[result.name] = result
        return result


class Application(metaclass=MetaApplication):
    name = None

    @staticmethod
    def populate_parser(parser):
        pass

    def __init__(self, manager):
        self.manager = manager
        self.running = threading.Event()

    def set_arguments(self, arguments):
        pass

    def set_options(self, options):
        pass

    def start(self):
        self.running.set()
        self.run()

    def stop(self):
        self.running.clear()