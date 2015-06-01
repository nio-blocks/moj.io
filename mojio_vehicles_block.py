from .mojio_base import MojioBase
from nio.common.discovery import Discoverable, DiscoverableType


@Discoverable(DiscoverableType.block)
class MojioVehicles(MojioBase):

    """ Notify details of connected moj.io vehicles """

    def _get_url_endpoint(self):
        return 'Vehicles'
