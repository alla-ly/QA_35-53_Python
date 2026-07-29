from unittest import TestCase
from Lesson6_OOP_unittest.oop.calculator_7 import Calculator


class TestCalculator(TestCase):
    def test_add(self):
        # calculator = Calculator()

        self.assertEqual(Calculator().add(2, 3), 5)
        # self.assertEqual(Calculator().add(2, 3), 4)

        # self.assertEqual(5, Calculator().add(2, 3))
        # self.assertEqual(4, Calculator().add(2, 3))

# assertEqual(a,b)
#assertEqual(2+2,4)
# assertTrue(x)
#
# def is_even(number):
# return number%2==0

# self.assertTrue(is_even(4))
# assertFalse(x)
# self.assertFalse(is_even(7))

#assertRaises
# def divide(a,b):
#     if b== 0:
#         raise ValueError ("Division by zero")
#     return a/b






















