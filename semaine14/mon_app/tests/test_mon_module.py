import unittest
from mon_package.mon_module import my_split, MyCustomTypeError

class TestMonModule(unittest.TestCase):
    
    def test_simple_input(self):
        input = "Bonjour à tous"
        output = my_split(input)
        expected = ['Bonjour', 'à', 'tous']
        self.assertEqual(output, expected)

    def test_is(self):
        a = [42]
        b = [42]
        c = a
        self.assertIs(a, c)
        self.assertIsNot(a, b)

    def test_boolean(self):
        a = False
        b = 0
        c = 1
        d = "Je suis une chaine de caractères"
        e = {}
        f = {"Ok"}
        self.assertFalse(a)
        self.assertFalse(b)
        self.assertTrue(c)
        self.assertTrue(d)
        self.assertFalse(e)
        self.assertTrue(f)

    def test_none(self):
        a = None
        b = 42
        self.assertIsNone(a)
        self.assertIsNotNone(b)

    def test_in(self):
        a = [1, 2, 3]
        self.assertIn(2, a)
        self.assertNotIn(4, a)

    def test_instance(self):
        a = 1
        self.assertIsInstance(a, int)
        self.assertNotIsInstance(a, float)

    def test_exception_if_not_string(self):
        input = 1
        self.assertRaises(MyCustomTypeError, my_split, input, "-")