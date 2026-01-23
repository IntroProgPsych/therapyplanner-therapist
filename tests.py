#import all needed modules here
import unittest
from app import Sessions


#write all your tests below this line
class TestSessions(unittest.TestCase):
    def test_low(self):
        self.assertEqual(Sessions(3), "Low")

    def test_moderate(self):
        self.assertEqual(Sessions(7), "Moderate")

    def test_high(self):
        self.assertEqual(Sessions(12), "High")

#write your test suite here, in the main() function
def main():
    #call all your tets here, one on each line
    print("Starting tests suite...")
    unittest.main()
    
#please do not change the lines below
if __name__ == "__main__":
    main()
