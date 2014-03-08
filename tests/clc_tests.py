import unittest
import clc


class TestBasicInput(unittest.TestCase):
    def setUp(self):
        self.c = clc.Clc()
        pass

    def test_initialize(self):
        self.assertIsNotNone(self.c)

        # Clc should initialize to have empty history and vars
        self.assertEqual(len(self.c.history), 0)
        self.assertEqual(len(self.c.vars), 0)

    def test_history(self):
        input1 = "2+2"
        self.c.push(input1)

        # pushing input1 should add it to the end of history
        self.assertEqual(self.c.history[-1], input1)

        count = 5
        l = len(self.c.history) + count
        input2 = "4+4"
        [self.c.push(input2) for i in range(count)]
        self.assertEqual(len(self.c.history), l)
        self.assertEqual(self.c.history[-1], input2)

    def test_basic_input(self):
        result = self.c.push("7")
        self.assertEqual(result, 7)

    def test_add(self):
        result = self.c.push("2+2")
        self.assertEqual(result, 4)

        result = self.c.push("2+3+4")
        self.assertEqual(result, 9)

    def test_subtract(self):
        result = self.c.push("5-4")
        self.assertEqual(result, 1)

        result = self.c.push("8-2+4-3+5")
        self.assertEqual(result, 12)

    def test_multiply(self):
        result = self.c.push("3*4")
        self.assertEqual(result, 12)

        input2 = "4*5+6"
        result = self.c.push(input2)
        self.assertEqual(result, 26)

    def test_divide(self):
        result = self.c.push("12/4")
        self.assertEqual(result, 3)

        input2 = "4*3/12*6/2"
        result = self.c.push(input2)
        self.assertEqual(result, 3)

    def test_order_of_operations(self):
        result = self.c.push("3*4+8*1-40/8")
        self.assertEqual(result, 15)

    def test_negative_number(self):
        result = self.c.push("-3+4")
        self.assertEqual(result, 1)


class TestParentheses(unittest.TestCase):
    def setUp(self):
        self.c = clc.Clc()

    def test_basic_input(self):
        result = self.c.push("(3)")
        self.assertEqual(result, 3)

        result = self.c.push("(((3)))")
        self.assertEqual(result, 3)

        result = self.c.push("(3")
        self.assertEqual(result, 3)

    def test_nested_operations(self):
        result = self.c.push("(3+4) * (3-2)")
        self.assertEqual(result, 7)

        result = self.c.push("(4*(3*2)*(((9/3)+2*4")
        self.assertEqual(result, 264)


class TestExponents(unittest.TestCase):
    def setUp(self):
        self.c = clc.Clc()

    def test_basic_exponent(self):
        result = self.c.push("2^2")
        self.assertEqual(result, 4)

    def test_nested_operations(self):
        result = self.c.push("((3^4*2)+2^3-1)^2")
        self.assertEqual(result, 28561)

    def test_fractional_exponent(self):
        result = self.c.push("4^0.5")
        self.assertEqual(result, 2)

    @unittest.skip("negatives are weird right now")
    def test_negative_exponent(self):
        result = self.c.push("4^-1")
        self.assertEqual(result, 0.25)
