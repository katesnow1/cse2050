import unittest
from process import Process

class TestProcess(unittest.TestCase):
    def test_init_one(self):
        """Tests initiliazation with just a name"""
        p1 = Process("hi")
        self.assertEqual(p1.pid, "hi")
        self.assertEqual(p1.cycles, 100)
        self.assertEqual(p1.link, None)
        self.assertEqual(p1.prev, None)
    
    def test_init_two(self):
        """Tests initiliazation with a name and cycles"""
        p1 = Process("bye", 120)
        self.assertEqual(p1.pid, "bye")
        self.assertEqual(p1.cycles, 120)
        self.assertEqual(p1.link, None)
        self.assertEqual(p1.prev, None)

    def test_eq(self):
        """Tests the eq method"""
        p1 = Process("hi", 190)
        p2 = Process("hi")
        p3 = Process("bye")
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

    def test_repr(self):
        """Tests the repr method"""
        p1 = Process("send_email")
        self.assertEqual(p1.__repr__(), "Process(send_email, 100)")


if __name__ == '__main__':
    unittest.main()
