import os

from setuptools import find_packages, setup

setup(
    name='k2-multirunner',
    version='0.0.1' + os.getenv('BUILD_NUMBER', '0'),
    description='Multi runner stub',
    maintainer='Patrik Dahlström',
    maintainer_email='risca@dalakolonin.se',
    license='Apache 2.0',
    packages=find_packages(
        exclude=[
            '*.test', '*.test.*', 'test.*', 'test', '*.systest', '*.systest.*', 'systest.*',
            'systest'
        ]),
    install_requires=[],
    entry_points={},
)
