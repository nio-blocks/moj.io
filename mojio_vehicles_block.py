from .mojio_base import MojioBase
from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties import VersionProperty


@Discoverable(DiscoverableType.block)
class MojioVehicles(MojioBase):

    """ Notify details of connected moj.io vehicles """
    version = VersionProperty('2.0.0')

    def _get_url_endpoint(self):
        return 'Vehicles'
