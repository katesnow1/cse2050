from doublylinkedlist import DoublyLinkedList as DLL
import unittest

class TestLinkedFactory:
    def setUp(self, _class):
        self._class = _class

    def test_init(self):
        ll1 = self._class()
        self.assertEqual(len(ll1), 0)
        self.assertEqual(ll1.get_head(), None)
        self.assertEqual(ll1.get_tail(), None)

    # Add other tests in this class as desired

    def test_add_first_one(self):
        ll1 = self._class()
        ll1.add_first('jake')
        self.assertEqual(len(ll1), 1)
        self.assertEqual(ll1.get_head().data, 'jake')
        self.assertEqual(ll1.get_head().link, None)
        self.assertEqual(ll1.get_tail().data, 'jake')

    def test_add_first_ten(self):
        ll1 = self._class()
        n = 10

        for i in range(n):
            ll1.add_first(i)
            self.assertEqual(len(ll1), i+1)
            self.assertEqual(ll1.get_head().data, i)
            self.assertEqual(ll1.get_tail().data, 0)

    def test_remove_first_one(self):
        ll1 = self._class()
        ll1.add_first('jake')

        self.assertEqual(ll1.remove_first(), 'jake')
        self.assertEqual(len(ll1), 0)
        self.assertEqual(ll1.get_head(), None)
        self.assertEqual(ll1.get_tail(), None)

    def test_add_first_remove_first_ten(self):
        ll1 = self._class()
        n = 10

        for i in range(n):
            ll1.add_first(i)
        #_head ->9->8->7...2->1->0->None

        for i in range(n):
            self.assertEqual(ll1.get_head().data, n-1-i)
            self.assertEqual(ll1.get_tail().data, 0)
            self.assertEqual(ll1.remove_first(), n-1-i)
            self.assertEqual(len(ll1), n-1-i)

        self.assertEqual(ll1.get_head(), None)
        self.assertEqual(ll1.get_tail(), None)

    def test_add_last_one(self):
        ll1 = self._class()
        ll1.add_last('jake')
        self.assertEqual(len(ll1), 1)
        self.assertEqual(ll1.get_head().data, 'jake')
        self.assertEqual(ll1.get_head().link, None)
        self.assertEqual(ll1.get_tail().data, 'jake')
        self.assertEqual(ll1.get_tail().link, None)

    def test_add_last_ten(self):
        ll1 = self._class()
        n = 10

        for i in range(n):
            ll1.add_last(i)
            self.assertEqual(len(ll1), i+1)
            self.assertEqual(ll1.get_head().data, 0)
            self.assertEqual(ll1.get_tail().data, i)
        # _head->0->1->2->...->8->9->None

    def test_add_last_remove_last(self):
        ll1 = self._class()
        n = 10

        for i in range(n):
            ll1.add_last(i)
            self.assertEqual(len(ll1), i+1)
        # _head->0->1->2->...->8->9->None
        
        for i in range(n):
            self.assertEqual(ll1.get_head().data, 0)
            self.assertEqual(ll1.get_tail().data, n-1-i)
            self.assertEqual(ll1.remove_last(), n-1-i)
            self.assertEqual(len(ll1), n-1-i)
            

class TestDoublyLinkedList(TestLinkedFactory, unittest.TestCase):
    def setUp(self):
        return TestLinkedFactory.setUp(self, DLL)


if __name__ == '__main__':
    unittest.main(verbosity=2)