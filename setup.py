#!/usr/bin/env python3

from setuptools import setup, Command, find_packages
import unittest


class RunServerCommand(Command):
    user_options = [
      # The format is (long option, short option, description).
      ('host=', 'H', 'rev3 host'),
      ('port=', 'p', 'rev3 port'),
      ('max-clients=', 'c', 'rev3 max client count'),
    ]

    def initialize_options(self):
        """Abstract method that is required to be overwritten"""
        self.host = ''
        self.port = '9999'
        self.max_clients = 1

    def finalize_options(self):
        """Abstract method that is required to be overwritten"""

    def run(self):
        import R_ev3dev
        print("start server host={} port={} max.clients={}".format(self.host, self.port, self.max_clients))
        server = R_ev3dev.server(host=self.host, port=int(self.port), max_clients=int(self.max_clients))
        server.run()


def project_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


setup(name='R_ev3dev',
      version="0.1",
      include_package_data=True,
      packages=find_packages(),
      test_suite="setup.project_test_suite",
      install_requires=['python-ev3dev2'],
      python_requires='>3.4.0',
      cmdclass={'run_server': RunServerCommand})
