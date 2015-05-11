from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType


@Discoverable(DiscoverableType.block)
class Mojio(Block):

    """ Connect to a Moj.io enabled automobile """

    def process_signals(self, signals, input_id='default'):
        pass
