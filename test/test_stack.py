import unittest

from parameterized import parameterized

from cls_stack.cls_stack import Stack

class TestFunction(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:  # before all tests
        cls.sample = Stack()

    @classmethod
    def tearDownClass(cls) -> None:  # after all tests
        print("End tests")

    @parameterized.expand(
        [
            ('{{[()]}}', 'balanced'),
            ('}{}', 'unbalanced')
        ]
    )
    def test_is_balanced(self, sample, result):
        self.assertMultiLineEqual(self.sample.is_balanced(sample), result)

    def test_isEmpty(self):
        tmp_sample = Stack()
        self.assertTrue(tmp_sample.isEmpty())

    def test_is_not_Empty(self):
        tmp_sample = Stack()
        tmp_sample.push(']')
        self.assertFalse(tmp_sample.isEmpty())




