import unittest
from app import app
from faker import Faker

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_sum(self):
        fake = Faker()
        num1 = fake.random_number(digits=3)
        num2 = fake.random_number(digits=3)
        sum = num1 + num2
        print(num1, num2)
        self.assertEqual(sum, num1 + num2)

if __name__ == '__main__':
    unittest.main()