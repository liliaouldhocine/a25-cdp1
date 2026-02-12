import unittest

class TestStringMethods(unittest.TestCase): 

    def test_upper(self):
        input = "foo"
        output = input.upper()
        expected = "FOO"
        self.assertEqual(output, expected)
    
    def test_is_upper(self):
        input = "FOO"
        self.assertTrue(input.isupper())
            
    def test_is_not_upper(self):
        input = "Foo"
        self.assertFalse(input.isupper())

    # un faux positif
    @unittest.skip("Ongoing implementation")
    def test_to_come(self):
        pass


if __name__ == "__main__":
    unittest.main()