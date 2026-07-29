import unittest


class TestNumbersList(unittest.TestCase):
    def setUp(self):
        print("Preparing the list")
        self.numbers = [1,2,3,4,5]

    def tearDown(self):
        print("Cleaning up")

    def test_list_has_five_items(self):
        self.assertEqual(len(self.numbers),5)

    def test_list_contains_three(self):
        self.assertIn(3, self.numbers)


