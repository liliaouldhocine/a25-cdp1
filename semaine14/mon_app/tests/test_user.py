import unittest
from mon_package.user import User
from mon_package.address import Address

class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("Avant le début des tests - TestUset")

    def setUp(self) -> None:
        print("Set Up")
        address = Address("Montréal", "Canadà")
        self.user = User("Lilia", address)
        
    def test_greetings(self):
        print("test_greetings")
        output = self.user.greetings()
        expected = "Bonjour Lilia"
        self.assertEqual(output, expected)

    def test_get_address(self):
        print("test_get_address")
        output = self.user.get_address()
        expected = "Montréal, Canadà"
        self.assertEqual(output,expected) 

    def tearDown(self) -> None:
        print("tearDown")
        # self.user = None

    @classmethod
    def tearDownClass(cls) -> None:
        print("Après les tests - TestUser")