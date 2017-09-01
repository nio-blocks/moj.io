from .mojio_base import MojioBase
from nio.signal.base import Signal
from nio.properties import VersionProperty


class MojioEvents(MojioBase):

    """ Notify events from connected moj.io vehicles """
    version = VersionProperty("2.0.0")

    def _get_url_endpoint(self):
        return 'Events'

    def _process_response(self, resp):
        fresh_posts = []
        posts = self._get_dicts_from_response(resp)

        if len(posts) > 0:
            self.update_freshness(posts)
            fresh_posts = self.find_fresh_posts(posts)
            paging = len(fresh_posts) == len(posts)

            # TODO: Make paging work - right now doing no paging
            paging = False

        self.logger.debug("Read {} posts, {} are fresh".format(
            len(posts), len(fresh_posts)))
        return [Signal(d) for d in fresh_posts], paging
