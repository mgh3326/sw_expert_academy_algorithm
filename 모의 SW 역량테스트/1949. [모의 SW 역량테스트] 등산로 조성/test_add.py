from unittest import TestCase

from main import add


class TestAdd(TestCase):
    def test_add(self):
        c = add(20, 10)
        self.assertEqual(c, 30)
