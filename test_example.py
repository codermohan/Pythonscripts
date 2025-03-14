import unittest
from day4 import greet_user,add_num,power  # Import the function from your Python script

class TestYourFunction(unittest.TestCase):
    
    def test_function(self):
        result = greet_user("Mohan")  # Call the function you're testing
        expected_result = "Hello Mohan!"
        self.assertEqual(result, expected_result)  # Replace expected_result with the correct value
        

if __name__ == '__main__':
    unittest.main()
