"""
Upgrade SUT software.

Interface addon for upgrading software on a SUT.
"""

import logging

from zaf.commands.command import CommandId
from zaf.config.options import ConfigOption, ConfigOptionId
from zaf.extensions.extension import FrameworkExtension, get_logger_name

from k2.sut import SUT
from upgrade.upgrader import Upgrader

logger = logging.getLogger(get_logger_name('k2', 'upgrade'))


def upgrade(core):
    """Upgrades SUTs with the given software."""
    software = core.config.get(UPGRADE_SOFTWARE)
    suts = core.config.get(SUT)

    error_occurred = False
    for sut in suts:
        try:
            upgrader = Upgrader(core.messagebus, sut, None)
            upgrader.perform_upgrade(software)
            logger.info(
                'Successfully upgraded sut {sut} with software \'{software}\''.format(
                    sut=sut, software=software))

        except Exception:
            logger.warning('Error upgrading sut {sut}'.format(sut=sut), exc_info=True)
            error_occurred = True

    return 1 if error_occurred else 0


UPGRADE_SOFTWARE = ConfigOptionId(
    'upgrade.software',
    'The software to upgrade to. Usully the path to an upgrade package.',
    option_type=str,
    argument=True)

UPGRADE_COMMAND = CommandId(
    'upgrade',
    upgrade.__doc__,
    upgrade,
    config_options=[
        ConfigOption(UPGRADE_SOFTWARE, required=True),
        ConfigOption(SUT, required=True)
    ],
    uses=['sut'])


@FrameworkExtension(
    name='upgrade',
    commands=[UPGRADE_COMMAND],
    groups=['upgrade'],
)
class UpgradeExtension(object):
    """Provides the upgrade command."""

    def __init__(self, config, instances):
        pass
