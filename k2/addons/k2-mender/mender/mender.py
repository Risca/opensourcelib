"""
Interact with Mender software update services.

Provides the necessary components and extensions to interact with the Mender client running on a SUT.
"""

import logging

from zaf.component.decorator import component, requires
from zaf.component.util import add_cans
from zaf.config.options import ConfigOption
from zaf.extensions.extension import AbstractExtension, CommandExtension, ExtensionConfig, \
    FrameworkExtension, get_logger_name
from zaf.messages.dispatchers import SequentialDispatcher
from zaf.messages.decorator import callback_dispatcher, sequential_dispatcher

from k2.cmd.run import RUN_COMMAND
from k2.sut import SUT
from mender import MENDER_BOOTLOADER, MENDER_ROOTFS, MENDER_UPGRADE_ENDPOINT
from mender.upgrader import MenderManualUpgrader, MenderTriggerUpgrader
from upgrade import AVAILABLE_UPGRADE_TYPES, K2_UPGRADE_COMPONENT, PERFORM_UPGRADE, UPGRADE_TYPE
from upgrade.upgradecommand import UPGRADE_COMMAND
from upgrade.upgrader import Upgrader

logger = logging.getLogger(get_logger_name('k2', 'mender'))
logger.addHandler(logging.NullHandler())


@CommandExtension(
    name='mender',
    extends=[RUN_COMMAND, UPGRADE_COMMAND],
    config_options=[
        ConfigOption(SUT, required=True, instantiate_on=True),
        ConfigOption(UPGRADE_TYPE, required=False),
        ConfigOption(MENDER_ROOTFS, required=False),
        ConfigOption(MENDER_BOOTLOADER, required=False),
    ],
    endpoints_and_messages={MENDER_UPGRADE_ENDPOINT: [PERFORM_UPGRADE]},
    groups=['upgrade'],
)
class MenderClient(AbstractExtension):
    """Mender client."""

    def __init__(self, config, instances):
        self.dispatcher = None
        self.is_active = False
        if 'mender' in config.get(UPGRADE_TYPE):
            self.is_active = True
            self.entity = instances[SUT]
            if config.get(UPGRADE_TYPE) == 'mender-trigger':
                self.upgrader = MenderTriggerUpgrader(entity=self.entity)
            elif config.get(UPGRADE_TYPE) == 'mender-manual':
                self.upgrader = MenderManualUpgrader(
                    entity=self.entity,
                    rootfs=config.get(MENDER_ROOTFS),
                    bootloader=config.get(MENDER_BOOTLOADER))

    def register_components(self, component_manager):
        if self.is_active:
            sut = component_manager.get_unique_class_for_entity(self.entity)
            add_cans(sut, ['upgrade'])

            @requires(sut='Sut', can=['upgrade'])
            @requires(messagebus='MessageBus')
            @component(name=K2_UPGRADE_COMPONENT, can=['upgrade'])
            def Mender(sut, messagebus):
                return Upgrader(messagebus, sut.entity, MENDER_UPGRADE_ENDPOINT)

    def register_dispatchers(self, messagebus):
        if self.is_active:
            self.dispatcher = SequentialDispatcher(messagebus, self.handle_message)
            self.dispatcher.register(
                [PERFORM_UPGRADE],
                [MENDER_UPGRADE_ENDPOINT],
                entities=[self.entity])

    def destroy(self):
        if self.is_active and self.dispatcher is not None:
            self.dispatcher.destroy()
            self.dispatcher = None

    @requires(events='SutEvents')
    @requires(exec='Exec')
    def handle_message(self, message, events, exec):
        return {PERFORM_UPGRADE: self.upgrader.perform_upgrade}[message.message_id](events, exec, message)


@FrameworkExtension(name='mender', groups=['upgrade'])
class MenderClientFrameworkExtension(object):
    """Provides the mender upgrade command."""

    def __init__(self, config, instances):
        pass

    def get_config(self, config, requested_config_options, requested_command_config_options):
        return ExtensionConfig(
            {
                AVAILABLE_UPGRADE_TYPES.name: ['mender-trigger', 'mender-manual']
            }, 1, 'mender')
