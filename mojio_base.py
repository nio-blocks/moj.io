from nio.metadata.properties import StringProperty
from nio.common.signal.base import Signal
from .http_blocks.rest.rest_block import RESTPolling

MOJIO_URL_BASE = 'https://api.moj.io/v1/'


class MojioBase(RESTPolling):

    """ A base block for making requests to the Moj.io API """

    api_key = StringProperty(title="API Key", default="[[MOJIO_TOKEN]]")

    def __init__(self):
        super().__init__()
        # We want the created at dates to be pulled out of the Time field
        self._created_field = 'Time'

    def _prepare_url(self, paging=False):
        self._url = "{}{}".format(MOJIO_URL_BASE, self._get_url_endpoint())

        return {
            'MojioAPIToken': self.api_key
        }

    def _process_response(self, resp):
        """ Overridden from RESTPolling - returns signals to notify """

        # By default, just return all of the signals we get, no paging
        return [Signal(d) for d in self._get_dicts_from_response(resp)], False

    def _get_dicts_from_response(self, resp):
        resp_data = resp.json()
        return resp_data['Data']

    def _get_url_endpoint(self):
        raise NotImplementedError
