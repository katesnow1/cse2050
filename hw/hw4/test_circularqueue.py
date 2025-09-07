import unittest
from circularqueue import CircularQueue
from process import Process

class TestCircularQueue(unittest.TestCase):
    def assertNodeEqual(self, node, expected, expected_prev, expected_link):
        """Checks if nodes are equal"""
        self.assertEqual(node, expected)
        self.assertEqual(node.prev, expected_prev)
        self.assertEqual(node.link, expected_link)

    def test_init(self):
        """Tests the initialization of a Circular Queue object"""
        cq1 = CircularQueue()
        self.assertEqual(cq1._head, None)
        self.assertEqual(len(cq1._d_processes), 0)
        p1 = Process("hi")
        p2 = Process("bye")
        cq2 = CircularQueue([p1, p2])
        self.assertNodeEqual(cq2._head, p1, p2, p2)

    def test_add_one(self):
        """Tests that a process is ended to the end of the queue"""
        cq1 = CircularQueue()
        n1 = Process("hi")
        n2 = Process("bye")
        n3 = Process("123")
        cq1.add_process(n1)
        self.assertNodeEqual(cq1._head, n1, n1, n1)
        self.assertEqual(len(cq1._d_processes), 1)
        cq1.add_process(n2)
        self.assertNodeEqual(cq1._head, n1, n2, n2)
        self.assertNodeEqual(cq1._head.link, n2, n1, n1)
        self.assertEqual(len(cq1._d_processes), 2)
        cq1.add_process(n3)
        self.assertNodeEqual(cq1._head, n1, n3, n2)
        self.assertNodeEqual(cq1._head.link, n2, n1, n3)
        self.assertNodeEqual(cq1._head.link.link, n3, n2, n1)
        self.assertEqual(len(cq1._d_processes), 3)

    def test_repr(self):
        """Tests that the correct string representation is returned"""
        cq1 = CircularQueue()
        n1 = Process("hi", 10)
        n2 = Process("bye")
        n3 = Process("123")
        cq1.add_process(n1)
        cq1.add_process(n2)
        cq1.add_process(n3)
        self.assertEqual(repr(cq1), "CircularQueue(Process(hi, 10), Process(bye, 100), Process(123, 100))")

    def test_remove_middle_process(self):
        cq1 = CircularQueue()
        n1 = Process("hi", 10)
        n2 = Process("bye")
        n3 = Process("123")
        cq1.add_process(n1)
        cq1.add_process(n2)
        cq1.add_process(n3)
        cq1.remove_process(n2)
        self.assertEqual(len(cq1._d_processes), 2)
        self.assertNodeEqual(cq1._head, n1, n3, n3)
        self.assertNodeEqual(cq1._head.link, n3, n1, n1)

    def test_remove_end_process(self):
        cq1 = CircularQueue()
        n1 = Process("hi", 10)
        n2 = Process("bye")
        n3 = Process("123")
        cq1.add_process(n1)
        cq1.add_process(n2)
        cq1.add_process(n3)
        cq1.remove_process(n3)
        self.assertEqual(len(cq1._d_processes), 2)
        self.assertNodeEqual(cq1._head, n1, n2, n2)
        self.assertNodeEqual(cq1._head.link, n2, n1, n1)

    def test_remove_start_process(self):
        cq1 = CircularQueue()
        n1 = Process("hi", 10)
        n2 = Process("bye")
        n3 = Process("123")
        cq1.add_process(n1)
        cq1.add_process(n2)
        cq1.add_process(n3)
        cq1.remove_process(n1)
        self.assertEqual(len(cq1._d_processes), 2)
        self.assertNodeEqual(cq1._head, n2, n3, n3)
        self.assertNodeEqual(cq1._head.link, n3, n2, n2)

    def test_remove_one_process(self):
        cq1 = CircularQueue()
        n1 = Process("hi", 10)
        cq1.add_process(n1)
        cq1.remove_process(n1)
        self.assertEqual(len(cq1._d_processes), 0)
        self.assertTrue(cq1._head is None)

    def test_kill(self):
        cq1 = CircularQueue()
        n1 = Process("hi", 10)
        n2 = Process("bye")
        n3 = Process("123")
        cq1.add_process(n1)
        cq1.add_process(n2)
        cq1.add_process(n3)
        cq1.kill("bye")
        self.assertEqual(len(cq1._d_processes), 2)
        self.assertNodeEqual(cq1._head, n1, n3, n3)
        self.assertNodeEqual(cq1._head.link, n3, n1, n1)


if __name__ == '__main__':
    unittest.main()


        