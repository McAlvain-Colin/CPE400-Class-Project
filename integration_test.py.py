import unittest

class TCPIntegrationTests(unittest.TestCase):
    def setUp(self):
        pass
    def myTest(self):
        a = 1
        self.assertEqual(a, 1)

if __name__ == "__main__":
    unittest.main()