from nio.properties import StringProperty, PropertyHolder, \
    ObjectProperty
from nio.signal.base import Signal
from nio.util.discovery import not_discoverable
from .rest_polling.rest_polling_base import RESTPolling
from .oauth2_mixin.oauth2_password import OAuth2PasswordGrant

MOJIO_URL_BASE = 'https://api.moj.io/v1/'


class MojioCreds(PropertyHolder):
    username = StringProperty(
        title="Moj.io Username", default="[[MOJIO_USERNAME]]")
    password = StringProperty(
        title="Moj.io Password", default="[[MOJIO_PASSWORD]]")
    client_id = StringProperty(
        title="Moj.io Client ID", default="[[MOJIO_CLIENT_ID]]")
    client_secret = StringProperty(
        title="Moj.io Client Secret", default="[[MOJIO_CLIENT_SECRET]]")


@not_discoverable
class MojioBase(OAuth2PasswordGrant, RESTPolling):

    """ A base block for making requests to the Moj.io API """

    creds = ObjectProperty(MojioCreds, title='Moj.io Credentials')

    def __init__(self):
        super().__init__()
        # We want the created at dates to be pulled out of the Time field
        self._created_field = 'Time'

    def get_oauth_base_url(self):
        return 'https://api.moj.io/OAuth2/'

    def _authenticate(self):
        """ Overridden from REST Polling block - get OAuth token here """
        try:
            token_info = self.get_access_token(
                username=self.creds().username(),
                password=self.creds().password(),
                addl_params={
                    'client_id': self.creds().client_id(),
                    'client_secret': self.creds().client_secret()
                })
            self.logger.debug("Token retrieved: {}".format(token_info))
        except:
            self.logger.exception("Error obtaining access token")

    def _prepare_url(self, paging=False):
        self._url = "{}{}".format(MOJIO_URL_BASE, self._get_url_endpoint())

        if not self.authenticated():
            self.logger.error("You must be authenticated to poll")
            return

        try:
            return {
                'MojioAPIToken': self._oauth_token.get('access_token')
            }
        except:
            self.logger.exception("Unable to set header with access token")

    def _process_response(self, resp):
        """ Overridden from RESTPolling - returns signals to notify """

        # By default, just return all of the signals we get, no paging
        return [Signal(d) for d in self._get_dicts_from_response(resp)], False

    def _get_dicts_from_response(self, resp):
        resp_data = resp.json()
        return resp_data['Data']

    def _get_url_endpoint(self):
        raise NotImplementedError
