from .mojio_base import MojioBase
from nio.util.discovery import discoverable
from nio.properties import VersionProperty


@discoverable
class MojioVehicles(MojioBase):

    """ Notify details of connected moj.io vehicles """
    version = VersionProperty('2.0.0')

    def _get_url_endpoint(self):
        return 'Vehicles'
