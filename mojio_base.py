from nio.metadata.properties import StringProperty
from nio.common.signal.base import Signal
from .oauth2_mixin.oauth2 import OAuth2
from .http_blocks.rest.rest_block import RESTPolling

MOJIO_URL_BASE = 'https://api.moj.io/v1/'


class MojioBase(RESTPolling, OAuth2):

    """ A base block for making requests to the Moj.io API """

    api_key = StringProperty(title="API Key", default="[[MOJIO_TOKEN]]")

    def _prepare_url(self, paging=False):
        self._url = "{}{}".format(MOJIO_URL_BASE, self._get_url_endpoint())

        return {
            'MojioAPIToken': self.api_key
        }

    def _process_response(self, resp):
        """ Overridden from RESTPolling - returns signals to notify """
        resp_data = resp.json()
        return [Signal(d) for d in resp_data['Data']], False
