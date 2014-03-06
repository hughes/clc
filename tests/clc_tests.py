import unittest
import clc


class TestSomething(unittest.TestCase):
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
        input1 = "7"
        result = self.c.push(input1)
        self.assertEqual(result, [7])

        input2 = "2+2"
        result = self.c.push(input2)
        self.assertEqual(result, [4])
