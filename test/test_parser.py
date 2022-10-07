import unittest
from vili.interfaces.common import DummyControllable
from vili.modules.parser import parse
from pathlib import Path

class TestParser(unittest.TestCase):

    def test_parser(self):
        sample_path = Path("vili/configs/dummy.yml")
        parsed = parse(sample_path)
        self.assertIsInstance(parsed["controllables"]["dummy1"], DummyControllable)
        self.assertIsInstance(parsed["controllables"]["dummy2"], DummyControllable)
        self.assertDictEqual(parsed["controllables"]["dummy2"].parameters, {"id": "random"})
        print(parsed)

if __name__ == '__main__':
    unittest.main()