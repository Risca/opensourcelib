import logging

from zaf.extensions.extension import get_logger_name

from upgrade import PERFORM_UPGRADE, UPGRADE_TIMEOUT

logger = logging.getLogger(get_logger_name('k2', 'upgrade'))


class NoUpgradeTypes(Exception):
    pass


class MultipleUpgradeTypes(Exception):
    pass


class Upgrader(object):

    def __init__(self, messagebus, entity, receiver_endpoint_id):
        self.messagebus = messagebus
        self.entity = entity
        self.receiver_endpoint_id = receiver_endpoint_id

    def _return_or_raise(self, futures):
        if len(futures) == 0:
            msg = 'Upgrade failed due to no upgrade types available for sut {sut}'.format(
                sut=self.entity)
            logger.warning(msg)
            raise NoUpgradeTypes(msg)
        elif len(futures) > 1:
            msg = 'Upgrade failed due to multiple upgrade types registered for sut {sut}'.format(
                sut=self.entity)
            logger.warning(msg)
            raise MultipleUpgradeTypes(msg)
        else:
            return futures[0].result(timeout=0)

    def perform_upgrade(self, software):
        """Perform software upgrade."""
        logger.info('Upgrading sut {sut}'.format(sut=self.entity))
        futures = self.messagebus.send_request(
            PERFORM_UPGRADE, self.receiver_endpoint_id, self.entity).wait(timeout=UPGRADE_TIMEOUT)
        return self._return_or_raise(futures)
