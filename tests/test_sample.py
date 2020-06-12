import unittest

from src.sample import Sample


class TestSample(unittest.TestCase):
    def test_sample_add(self):
        # Sample.add は空の実装なので、その修正しない限りこのテストは失敗します！
        self.assertEqual(7, Sample().add(3, 4))
