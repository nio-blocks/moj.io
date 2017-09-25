from .mojio_base import MojioBase
from nio.properties import VersionProperty


class MojioVehicles(MojioBase):

    """ Notify details of connected moj.io vehicles """
    version = VersionProperty("2.0.2")

    def _get_url_endpoint(self):
        return 'Vehicles'
