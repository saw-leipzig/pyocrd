from ocrd.resolver import Resolver
from ocrd.processor.base import Processor

from test.base import TestCase, assets, main

class DummyProcessor(Processor):

    def __init__(self, *args, **kwargs):
        kwargs['ocrd_tool'] = {
            'executable': 'ocrd-test'
        }
        kwargs['version'] = '0.0.1'
        super(DummyProcessor, self).__init__(*args, **kwargs)

class TestResolver(TestCase):

    def setUp(self):
        self.resolver = Resolver()
        self.workspace = self.resolver.workspace_from_url(assets.url_of('SBB0000F29300010000/mets.xml'))

    def test_verify(self):
        proc = DummyProcessor(self.workspace)
        self.assertEquals(proc.verify(), True)

    def test_json(self):
        DummyProcessor(self.workspace, dump_json=True)

    def test_params(self):
        proc = Processor(workspace=self.workspace)
        self.assertEquals(proc.parameter, {})

