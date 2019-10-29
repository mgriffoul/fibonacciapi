import unittest

from app.service import fetch_closer


class MyTestCase(unittest.TestCase):
    def test_fetchCloserShouldReturn0_whenSubmitIs0(self):
        self.assertEqual(fetch_closer(0), 0)

    def test_fetchCloserShouldReturn1_whenSubmitIs1(self):
        self.assertEqual(fetch_closer(1), 1)

    def test_fetchCloserShouldReturn2_whenArgIs2(self):
        self.assertEqual(fetch_closer(2), 2)

    def test_fetchCloserShouldReturn13_whenArgIs13(self):
        self.assertEqual(fetch_closer(13), 13)

    def test_fetchCloserShouldReturn13_whenArgIs14(self):
        self.assertEqual(fetch_closer(14), 13)

    def test_fetchCloserShouldReturn21_whenArgIs18(self):
        self.assertEqual(fetch_closer(18), 21)


if __name__ == '__main__':
    unittest.main()
