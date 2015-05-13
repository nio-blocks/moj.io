import responses
import json
from collections import defaultdict
from nio.common.signal.base import Signal
from nio.util.support.block_test_case import NIOBlockTestCase
from ..mojio_vehicles_block import MojioVehicles

SAMPLE_RESPONSE = {
    "PageSize": 10,
    "Offset": 0,
    "TotalRows": 1,
    "Data": [
        {
            "Type": "Vehicle",
            "OwnerId": "4add953e-6475-42b6-b4ba-d85e193dd644",
            "MojioId": "FAKE-MOJIO-ID",
            "Name": "Scion"
        }
    ]
}


class TestMojioVehicles(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        # This will keep a list of signals notified for each output
        self.last_notified = defaultdict(list)

    def signals_notified(self, signals, output_id='default'):
        self.last_notified[output_id].extend(signals)

    @responses.activate
    def test_request(self):
        blk = MojioVehicles()

        responses.add(responses.GET, 'https://api.moj.io/v1/Vehicles',
                      body=json.dumps(SAMPLE_RESPONSE), status=200,
                      content_type='application/json')
        self.configure_block(blk, {
            'polling_interval': {
                'seconds': 0  # We will drive polls with signals
            },
            'queries': ['dummy']
        })
        blk.start()

        blk.process_signals([Signal()])
        self.assert_num_signals_notified(1)
        self.assertEqual(self.last_notified['default'][0].MojioId,
                         'FAKE-MOJIO-ID')

        blk.stop()
