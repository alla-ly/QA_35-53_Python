import unittest


class TestThreeChecks(unittest.TestCase):
    def setUp(self):
        print("setUp called")

    def testDown(self):
        print("tearDoun called")

    def test_one(self):
        print("test_one running")

    def test_two(self):
        print("test_two running")

    def test_three(self):
        print("test_three running")