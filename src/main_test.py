import unittest

from .main import my_sum


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(my_sum(1, 0), 1)


if __name__ == '__main__':
    unittest.main()

