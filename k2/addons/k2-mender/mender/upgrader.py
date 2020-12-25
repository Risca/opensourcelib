from upgrade import UPGRADE_TIMEOUT

class MenderTriggerUpgrader(object):
    """Tell the Mender client to check for new software."""

    def __init__(self, entity):
        self.entity = entity

    def perform_upgrade(self, sut_events, exec, software):
        with sut_events.await_sut_reset_done(timeout=UPGRADE_TIMEOUT):
            exec.send_line('pkill -USR1 mender')


class MenderManualUpgrader(object):
    """Manually upgrade the inactive rootfs, switch boot device, and reboot."""

    def __init__(self, entity, rootfs, bootloader):
        self.entity = entity
        self.rootfs = rootfs
        self.bootloader = bootloader

    def perform_upgrade(self, sutevents, exec, software):
        raise NotImplementedError('Mender manual upgrade not implemented')
