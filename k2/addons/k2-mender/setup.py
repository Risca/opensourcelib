import os

from setuptools import find_packages, setup

setup(
    name='mender',
    version='0.0.1' + os.getenv('BUILD_NUMBER', '0'),
    description='Interact with Mender software update services',
    long_description=(
        'Provides the necessary components and extensions to interact with the Mender client running on a SUT.'
    ),
    maintainer='Patrik Dahlström',
    maintainer_email='risca@dalakolonin.se',
    license='Apache 2.0',
    packages=find_packages(
        exclude=[
            '*.test', '*.test.*', 'test.*', 'test', '*.systest', '*.systest.*', 'systest.*',
            'systest'
        ]),
    install_requires=[''],
    entry_points={
        'k2.addons': [
            'menderclient = mender.mender:MenderClient',
            'menderclientextension = mender.mender:MenderClientFrameworkExtension',
        ],
    },
)
