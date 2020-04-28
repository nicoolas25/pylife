import life
import unittest

class TestLife(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(life.func(3), 5)
