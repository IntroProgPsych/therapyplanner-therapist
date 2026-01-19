#import all needed modules here
import unittest
from app import interpret


#write all your tests below this line
class TestInterpret(unittest.TestCase):
    def test_low(self):
        self.assertEqual(interpret(3), "Low")

    def test_moderate(self):
        self.assertEqual(interpret(7), "Moderate")

    def test_high(self):
        self.assertEqual(interpret(12), "High")

#write your test suite here, in the main() function
def main():
    #call all your tets here, one on each line
    print("Starting tests suite...")
    unittest.main()
    
#please do not change the lines below
if __name__ == "__main__":
    main()
