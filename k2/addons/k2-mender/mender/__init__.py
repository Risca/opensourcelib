from zaf.config.options import ConfigOptionId
from zaf.config.types import Choice
from zaf.messages.message import EndpointId

from k2.sut import SUT

MENDER_ROOTFS = ConfigOptionId(
    'mender.rootfs',
    'What kind of rootfs is the SUT using',
    at=SUT,
    option_type=Choice(['sdcard', 'ubi']),
    default='ubi')

MENDER_BOOTLOADER = ConfigOptionId(
    'mender.bootloader',
    """\
    What kind of bootloader is the SUT using.

    This configures how the Mender client updates which rootfs device to boot.
    """,
    at=SUT,
    option_type=Choice(['grub', 'uboot']),
    default='uboot')

MENDER_UPGRADE_ENDPOINT = EndpointId(
    'mender', 'Endpoint for software update using the Mender client.')
